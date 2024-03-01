# Standard Imports
import os, sys
from pathlib import Path
import time
import clr

dll_dir = os.path.join(os.getcwd(), 'autonomous_robotic_sample_handling', 'API', '')

ref_DeviceManagerCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.DeviceManagerCLI")
ref_GenericMotorCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.GenericMotorCLI")
ref_StepperMotorCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.Benchtop.StepperMotorCLI")

clr.AddReference(ref_DeviceManagerCLI)
clr.AddReference(ref_GenericMotorCLI)
clr.AddReference(ref_StepperMotorCLI)

# from Thorlabs.MotionControl.DeviceManagerCLI import BuildDeviceList
# from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import MotorDirection as MD
# from Thorlabs.MotionControl.Benchtop.StepperMotorCLI import BenchtopStepperMotor
from System import Decimal

class Motor:
    def __init__(self, device_connection, *args):
        # DeviceManagerCLI.BuildDeviceList()
        configuration = args[0]
        self.device = device_connection
        self.MotorDirection = MD
        self.timeoutVal = 60000

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


    def home(self):
        print("Homing Motor")
        self.channel.Home(self.timeoutVal)
        print("finish homing")

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
            "moveJog": lambda *args: self.MoveJog()
        }