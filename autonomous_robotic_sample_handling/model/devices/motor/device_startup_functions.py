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
from pathlib import Path
import clr

# Third party imports

# Local application imports
from navigate.tools.common_functions import load_module_from_file
from navigate.tools.file_functions import load_yaml_file
from navigate.config.config import get_navigate_path
from navigate.model.device_startup_functions import (
    device_not_found,
    DummyDeviceConnection,
    auto_redial,
)

# Same as in configuration.yaml, e.g. "stage", "filter_wheel", "remote_focus_device"...
DEVICE_TYPE_NAME = "motor"

# the reference value from configuration.yaml
DEVICE_REF_LIST = ["type"]


def build_motor_connection(configuration, motor, motor_serial_no):
    motor.Connect(motor_serial_no)
    return motor


def load_device(configuration, is_synthetic=False):
    """Load the Stepper Motor

    Parameters
    ----------
    configuration : dict
        The configuration for the Robot Arm
    is_synthetic : bool
        Whether the device is synthetic or not. Default is False.

    Returns
    -------
    object
        The device connection object
    """

    plugins_config_path = os.path.join(
        get_navigate_path(), "config", "plugins_config.yml"
    )

    plugins_config = load_yaml_file(plugins_config_path)
    plugin_path = plugins_config["Autonomous Robotic Sample Handling"]

    if is_synthetic:
        motor_type = "SyntheticMotor"
    else:
        # Can be Meca500, SyntheticRobot, syntheticrobot, Synthetic, synthetic
        motor_type = configuration.get("type", "HDR50")

    if motor_type == "HDR50":
        from Thorlabs.MotionControl.DeviceManagerCLI import DeviceManagerCLI
        from Thorlabs.MotionControl.Benchtop.StepperMotorCLI import BenchtopStepperMotor

        motor_serial_no = configuration["serial_no"]
        dll_dir = os.path.join(plugin_path, "API")
        ref_device_manager_cli = os.path.join(
            dll_dir, "Thorlabs.MotionControl.DeviceManagerCLI.dll"
        )
        ref_stepper_motor_cli = os.path.join(
            dll_dir, "Thorlabs.MotionControl.Benchtop.StepperMotorCLI.dll"
        )

        clr.AddReference(ref_device_manager_cli)
        clr.AddReference(ref_stepper_motor_cli)
        DeviceManagerCLI.BuildDeviceList()
        motor = BenchtopStepperMotor.CreateBenchtopStepperMotor(motor_serial_no)

        return auto_redial(
            build_motor_connection,
            (
                configuration,
                motor,
                motor_serial_no,
            ),
            exception=Exception,
        )

    elif motor_type.lower() == "SyntheticMotor" or motor_type.lower() == "synthetic":
        return DummyDeviceConnection()


def start_device(microscope_name, device_connection, configuration, is_synthetic=False):
    """Start the Robot Arm

    Parameters
    ----------
    microscope_name : str
        The name of the microscope
    device_connection : object
        The device connection object
    configuration : dict
        The configuration for the Robot Arm
    is_synthetic : bool
        Whether the device is synthetic or not. Default is False.

    Returns
    -------
    object
        The Robot Arm object
    """
    if is_synthetic:
        device_type = "synthetic"
    else:
        device_type = configuration["configuration"]["microscopes"][microscope_name][
            "motor"
        ]["hardware"]["type"]

    if device_type == "HDR50":
        motor = load_module_from_file(
            "motor",
            os.path.join(Path(__file__).resolve().parent, "motor.py"),
        )
        return motor.Motor(
            device_connection,
            configuration["configuration"]["microscopes"][microscope_name]["motor"],
        )
    elif device_type == "synthetic":
        synthetic_device = load_module_from_file(
            "synthetic_device",
            os.path.join(Path(__file__).resolve().parent, "synthetic_device.py"),
        )
        return synthetic_device.SyntheticRobotArm(
            device_connection,
            configuration["configuration"]["microscopes"][microscope_name]["motor"],
        )
    else:
        return device_not_found(microscope_name, device_type)
