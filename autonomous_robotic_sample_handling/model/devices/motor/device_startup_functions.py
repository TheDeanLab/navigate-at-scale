# Standard Imports
import os
from pathlib import Path
import time
import clr

from navigate.tools.common_functions import load_module_from_file
from navigate.model.device_startup_functions import device_not_found

from autonomous_robotic_sample_handling.API import Thorlabs.MotionControl.DeviceManagerCLI.dll
from autonomous_robotic_sample_handling.API import Thorlabs.MotionControl.GenericMotorCLI.dll
from autonomous_robotic_sample_handling.API import Thorlabs.MotionControl.Benchtop.StepperMotorCLI.dll

clr.AddReference("Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("Thorlabs.MotionControl.Benchtop.StepperMotorCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import MotorDirection as MD
from Thorlabs.MotionControl.Benchtop.StepperMotorCLI import *
#from System import Decimal  # necessary for real world units
from System import Decimal

DEVICE_TYPE_NAME = "rotary_stage"  # Same as in configuraion.yaml, for example "stage", "filter_wheel", "remote_focus_device"...
DEVICE_REF_LIST = ["type"]  # the reference value from configuration.yaml


def load_device(configuration, is_synthetic=False):
    """Build device connection.

    Returns
    -------
    device_connection : object
    """
    serial_no = "40405424"
    DeviceManagerCLI.BuildDeviceList()
    device = BenchtopStepperMotor.CreateBenchtopStepperMotor(self.serial_no)
    device.Connect(self.serial_no)
    
    channel = self.device.GetChannel(1)
    
    #Check if Controller Initializes Rotary Stage
    if not channel.IsSettingsInitialized():
        channel.WaitForSettingsInitialized(10000)  # 10 second timeout
        assert channel.IsSettingsInitialized() is True
    
    # Start polling and enable
    channel.StartPolling(250)  #250ms polling rate
    time.sleep(5)
    channel.EnableDevice()
    time.sleep(0.25)  # Wait for device to enable
    
    device_info = channel.GetDeviceInfo()
    print(device_info)
    print(device_info.Description)
    
    
    # Load any configuration settings needed by the controller/stage
    channel_config = channel.LoadMotorConfiguration(serial_no) # If using BSC203, change serial_no to channel.DeviceID. 
    chan_settings = channel.MotorDeviceSettings

    channel.GetSettings(chan_settings)
    channel_config.DeviceSettingsName = 'HDR50'
    channel_config.UpdateCurrentConfiguration()
    channel.SetSettings(chan_settings, True, False)
    return type("DeviceConnection", (object,), {})


def start_device(microscope_name, device_connection, configuration, is_synthetic=False):
    """Start device.

    Returns
    -------
    device_object : object
    """
    if is_synthetic:
        device_type = "synthetic"
    else:
        device_type = configuration["configuration"]["microscopes"][microscope_name][
            "rotary_stage"
        ]["hardware"]["type"]

    if device_type == "PluginDevice":
        plugin_device = load_module_from_file(
            "robot_arm",
            os.path.join(Path(__file__).resolve().parent, "plugin_device.py"),
        )
        return plugin_device.PluginDevice(device_connection=device_connection)
    elif device_type == "synthetic":
        synthetic_device = load_module_from_file(
            "synthetic_device",
            os.path.join(Path(__file__).resolve().parent, "synthetic_device.py"),
        )
        return synthetic_device.SyntheticDevice(device_connection=device_connection)
    else:
        return device_not_found(microscope_name, device_type)
