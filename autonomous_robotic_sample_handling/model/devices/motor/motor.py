# Standard Imports
import os

from navigate.tools.file_functions import load_yaml_file
from navigate.config.config import get_navigate_path

from pathlib import Path
import time
import clr

plugins_config_path = os.path.join(
        get_navigate_path(), "config", "plugins_config.yml"
    )
    
plugins_config = load_yaml_file(plugins_config_path)
plugin_path = plugins_config["Autonomous Robotic Sample Handling"]
    

dll_dir = os.path.join(plugin_path, 'API')

ref_DeviceManagerCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.DeviceManagerCLI")
ref_GenericMotorCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.GenericMotorCLI")
ref_StepperMotorCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.Benchtop.StepperMotorCLI")

clr.AddReference(ref_DeviceManagerCLI)
clr.AddReference(ref_GenericMotorCLI)
clr.AddReference(ref_StepperMotorCLI)

# from Thorlabs.MotionControl.DeviceManagerCLI import BuildDeviceList
# from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import MotorDirection as MD
# from ThorLabs.MotionControl.GenericMotorCLI import Settings
# from ThorLabs.MotionControl.GenericMotorCLI import RotationDirections as RD
# from Thorlabs.MotionControl.Benchtop.StepperMotorCLI import BenchtopStepperMotor
from System import Decimal

class Motor:
    def __init__(self, device_connection, *args):
        # DeviceManagerCLI.BuildDeviceList()
        motor_configuration = args[0]
        self.device = device_connection
        self.MotorDirection = MD
        # self.RotationDirections = Settings.RotationSettings.RotationDirections
        # self.RotationMode = RD
        self.timeoutVal = 100000
        self.serial_no = motor_configuration['hardware']['serial_no']

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

        self.device_info = self.channel.GetDeviceInfo()
        print(self.device_info)
        print(self.device_info.Description)

        # Load any configuration settings needed by the controller/stage
        self.channel_config = self.channel.LoadMotorConfiguration(
            self.serial_no)  # If using BSC203, change serial_no to channel.DeviceID.
        self.chan_settings = self.channel.MotorDeviceSettings

        self.channel.GetSettings(self.chan_settings)
        self.channel_config.DeviceSettingsName = 'HDR50'
        self.channel_config.UpdateCurrentConfiguration()
        self.channel.SetSettings(self.chan_settings, True, False)
        self.home()


    def home(self):
        print("Homing Motor")
        # self.channel.SetRotationModes(self.RotationMode.RotationalRange,self.RotationDirection.Quickest)
        self.channel.Home(self.timeoutVal)
        print("finish homing")
        self.channel.ResetRotationModes()


    def MoveJog(self,MotorDirection):
        
         #Pass string or initialize MotorDirection.Forward/Backward outside?
         
        if MotorDirection == "Forward":
            self.channel.MoveJog(self.MotorDirection.Forward,self.timeoutVal)
        else:
            self.channel.MoveJog(self.MotorDirection.Backward,self.timeoutVal)

        
    def MoveTo(self,Position):
        print("moving")
        self.channel.MoveTo(Decimal(Position),self.timeoutVal)
        print("Moving success")

    def disconnect(self):
        self.channel.StopPolling()
        self.device.Disconnect()
        
    def getPosition(self):
        
        return self.channel.Position
    
    def SetJogStepSize(self,JogStepSize):
        
        self.channel.SetJogStepSize(Decimal(JogStepSize))
        
    def SetJogVelocityParams(self,JogVelocity,JogAccel):
        
        self.SetJogVelocityParams(Decimal(JogVelocity),Decimal(JogAccel))
    
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
            "moveJog": lambda *args: self.MoveJog(args[0]),
            "position": lambda *args: self.getPosition(),
            "moveTo": lambda *args: self.MoveTo(args[0][0])
        }