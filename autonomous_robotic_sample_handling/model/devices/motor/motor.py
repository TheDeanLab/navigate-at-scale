# Copyright (c) 2021-2024  The University of Texas Southwestern Medical Center.
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted for academic and research use only
# (subject to the limitations in the disclaimer below)
# provided that the following conditions are met:

#      * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.

#      * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.

#      * Neither the name of the copyright holders nor the names of its
#      contributors may be used to endorse or promote products derived from this
#      software without specific prior written permission.

# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Standard Imports
import os
import time
from System import Decimal

# Third party imports
import clr
from Thorlabs.MotionControl.GenericMotorCLI import MotorDirection as MD

# Local application imports
from navigate.tools.file_functions import load_yaml_file
from navigate.config.config import get_navigate_path

plugins_config_path = os.path.join(get_navigate_path(), "config", "plugins_config.yml")

plugins_config = load_yaml_file(plugins_config_path)
plugin_path = plugins_config["Autonomous Robotic Sample Handling"]

dll_dir = os.path.join(plugin_path, "API")

ref_DeviceManagerCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.DeviceManagerCLI")
ref_GenericMotorCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.GenericMotorCLI")
ref_StepperMotorCLI = os.path.join(
    dll_dir, "Thorlabs.MotionControl.Benchtop.StepperMotorCLI"
)

clr.AddReference(ref_DeviceManagerCLI)
clr.AddReference(ref_GenericMotorCLI)
clr.AddReference(ref_StepperMotorCLI)


class Motor:
    """Motor Class"""

    def __init__(self, device_connection, *args):
        """Initialize Motor

        Parameters
        ----------
        device_connection : object
            device connection object
        args : list
            arguments for the device
        """
        motor_configuration = args[0]

        #: object: The device connection object
        self.device = device_connection

        self.MotorDirection = MD

        #: int: The timeout value in milliseconds
        self.timeoutVal = 100000

        #: str: The serial number
        self.serial_no = motor_configuration["hardware"]["serial_no"]

        #: object: The device channel
        self.channel = self.device.GetChannel(1)

        # Check if Controller Initializes Rotary Stage
        if not self.channel.IsSettingsInitialized():
            self.channel.WaitForSettingsInitialized(10000)  # 10 second timeout
            assert self.channel.IsSettingsInitialized() is True

        # Start polling and enable
        self.channel.StartPolling(250)  # 250ms polling rate
        time.sleep(5)
        self.channel.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable

        #: object: The device information
        self.device_info = self.channel.GetDeviceInfo()

        # Load any configuration settings needed by the controller/stage
        #: object: The channel configuration
        self.channel_config = self.channel.LoadMotorConfiguration(
            self.serial_no
        )  # If using BSC203, change serial_no to channel.DeviceID.

        #: object: The channel settings
        self.chan_settings = self.channel.MotorDeviceSettings

        self.channel.GetSettings(self.chan_settings)
        self.channel_config.DeviceSettingsName = "HDR50"
        self.channel_config.UpdateCurrentConfiguration()
        self.channel.SetSettings(self.chan_settings, True, False)
        self.set_homing_velocity(20)
        self.home()

    def home(self):
        """Home the motor"""
        self.channel.Home(self.timeoutVal)
        self.channel.ResetRotationModes()

    def move_jog(self, motor_direction):
        """Move the motor in the specified direction.

        Parameters
        ----------
        motor_direction : str
            The direction to move the motor in
        """
        if motor_direction == "Forward":
            self.channel.move_jog(self.MotorDirection.Forward, self.timeoutVal)
        else:
            self.channel.move_jog(self.MotorDirection.Backward, self.timeoutVal)

    def set_homing_velocity(self, velocity):
        """Set the homing velocity.

        Parameters
        ----------
        velocity : int
            The homing velocity
        """
        self.channel.SetHomingVelocity(Decimal(velocity))

    def move_to(self, position):
        """Move the motor to the specified position.

        Parameters
        ----------
        position : int
            The position to move the motor to
        """
        self.channel.move_to(Decimal(position), self.timeoutVal)

    def disconnect(self):
        """Disconnect the motor"""
        self.channel.StopPolling()
        self.device.Disconnect()

    def get_position(self):
        """Get the motor position.

        Returns
        -------
        int
            The motor position
        """
        return self.channel.Position

    def set_jog_step_size(self, jog_step_size):
        """Set the jog step size.

        Parameters
        ----------
        jog_step_size : int
            The jog step size
        """
        self.channel.set_jog_step_size(Decimal(jog_step_size))

    def set_jog_velocity_parameters(self, jog_velocity, jog_acceleration):
        """Set the jog velocity parameters.

        Parameters
        ----------
        jog_velocity : int
            The jog velocity
        jog_acceleration : int
            The jog acceleration
        """
        self.set_jog_velocity_parameters(
            Decimal(jog_velocity), Decimal(jog_acceleration)
        )

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {
            "home": lambda *args: self.home(),
            "disconnect": lambda *args: self.disconnect(),
            "moveJog": lambda *args: self.move_jog(args[0]),
            "position": lambda *args: self.get_position(),
            "moveTo": lambda *args: self.move_to(args[0]),
            "setHomingVelocity": lambda *args: self.set_homing_velocity(args[0]),
        }
