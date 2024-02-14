# Standard Imports
import os
from pathlib import Path

# Third party imports
# import mecademicpy.robot as mdr
# from tkinter import messagebox

# Local application imports
from navigate.tools.common_functions import load_module_from_file
from navigate.model.device_startup_functions import (
    device_not_found,
    DummyDeviceConnection,
)

DEVICE_TYPE_NAME = "robot_arm"  # Same as in configuraion.yaml, for example "stage", "filter_wheel", "remote_focus_device"...
DEVICE_REF_LIST = ["type"]  # the reference value from configuration.yaml


def load_device(configuration, is_synthetic=False):
    """ Load the Robot Arm

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
    # print("*** loading connection to robo arm!")
    # if is_synthetic:
    #     device_type = "synthetic"
    # else:
    #     device_type = configuration["configuration"]["microscopes"][microscope_name]["robot_arm"]["hardware"]["type"]
    # return DummyDeviceConnection()

    if is_synthetic:
        print("*** Building Synthetic Connection")
        return DummyDeviceConnection()
    else:
        module = load_module_from_file("robot_arm", r"C:\Kushal\10-19 College\17 Fall 2023\Senior Design I\navigate-at-scale\autonomous_robotic_sample_handling\model\devices\robot_arm\robot_arm.py")
        return module.connect_to_robot_arm(None)
    pass

def start_device(microscope_name, device_connection, configuration, is_synthetic=False):
    """ Start the Robot ARm

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
        device_type = configuration["configuration"]["microscopes"][microscope_name]["robot_arm"]["hardware"]["type"]

    if device_type == "Meca500":
        robot_arm = load_module_from_file(
            "robot_arm",
            os.path.join(Path(__file__).resolve().parent, "robot_arm.py"),
        )
        return robot_arm.RobotArm(device_connection=device_connection)
    elif device_type == "synthetic":
        synthetic_device = load_module_from_file(
            "synthetic_device",
            os.path.join(Path(__file__).resolve().parent, "synthetic_device.py"),
        )
        return synthetic_device.SyntheticRobotArm(device_connection=device_connection)
    else:
        return device_not_found(microscope_name, device_type)
