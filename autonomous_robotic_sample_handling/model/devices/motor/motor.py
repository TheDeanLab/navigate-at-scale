# Standard Imports
import os, sys
from pathlib import Path
import time
import clr

# dll_dir = os.path.join(os.getcwd(), 'autonomous_robotic_sample_handling', 'API', '')
# #TODO: Figure out an easier/more elegant way to join paths. The .s in the dll file name is problematic?
# print(dll_dir)
#
# ref_DeviceManagerCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.DeviceManagerCLI")
# ref_GenericMotorCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.GenericMotorCLI")
# ref_StepperMotorCLI = os.path.join(dll_dir, "Thorlabs.MotionControl.Benchtop.StepperMotorCLI")

# DeviceManagerCLI = r'%s%s' % (dll_dir, "Thorlabs.MotionControl.DeviceManagerCLI")
# os.path.relpath("./autonomous_robotic_sample_handling/API/Thorlabs.MotionControl.DeviceManagerCLI.dll")
# GenericMotorCLI = r'%s%s' % (dll_dir, "Thorlabs.MotionControl.GenericMotorCLI")
# os.path.relpath("./autonomous_robotic_sample_handling/API/Thorlabs.MotionControl.GenericMotorCLI.dll")
# StepperMotorCLI = r'%s%s' % (dll_dir, "Thorlabs.MotionControl.StepperMotorCLI")
# os.path.relpath("./autonomous_robotic_sample_handling/API/Thorlabs.MotionControl.StepperMotorCLI.dll")

# print(ref_DeviceManagerCLI)
# sys.path.append(dll_dir)

# clr.AddReference(ref_DeviceManagerCLI)
# clr.AddReference(ref_GenericMotorCLI)
# clr.AddReference(ref_StepperMotorCLI)

clr.AddReference(r"C:\\Kushal\\10-19 College\\17 Fall 2023\\Senior Design I\\navigate-at-scale\\autonomous_robotic_sample_handling\\API\\Thorlabs.MotionControl.Benchtop.StepperMotorCLI.dll")
clr.AddReference(r"C:\\Kushal\\10-19 College\\17 Fall 2023\\Senior Design I\\navigate-at-scale\\autonomous_robotic_sample_handling\\API\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference(r"C:\\Kushal\\10-19 College\\17 Fall 2023\\Senior Design I\\navigate-at-scale\\autonomous_robotic_sample_handling\\API\\Thorlabs.MotionControl.DeviceMangerCLI.dll")


from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import MotorDirection as MD
from Thorlabs.MotionControl.Benchtop.StepperMotorCLI import *
from System import Decimal

class Motor():
    def __init__(self):
        self.serial_no = "40405424"
        DeviceManagerCLI.BuildDeviceList()
        self.device = BenchtopStepperMotor.CreateBenchtopStepperMotor(self.serial_no)
        self.device.Connect(self.serial_no)
        self.MotorDirection = MD

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
        self.channel.Home(60000)

    def MoveJog(self):
        print("MOVE JOG ENTER")
        print(self.MotorDirection.Forward)
        self.channel.MoveJog(self.MotorDirection.Forward, 100000)
        print("MOVING ROTARY")

    def disconnect(self):
        self.channel.StopPolling()
        self.device.Disconnect()

    def loop(self):
        while True:
            self.MoveJog()