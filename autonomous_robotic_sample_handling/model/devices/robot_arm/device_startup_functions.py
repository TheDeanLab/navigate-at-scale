# Standard Imports
import os
from pathlib import Path

# Third party imports
# from tkinter import messagebox

# Local application imports
from navigate.tools.common_functions import load_module_from_file
from navigate.model.device_startup_functions import (
    device_not_found,
    DummyDeviceConnection,
    auto_redial
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
    if is_synthetic:
        robot_type = "SyntheticRobot"
    else:
        # Can be Meca500, SyntheticRobot, syntheticrobot, Synthetic, synthetic
        robot_type = configuration["configuration"]["hardware"]["robot_arm"]["type"]

    if robot_type == "Meca500":
        #TODO: Consider auto_redial function.
        robot_ip_address = configuration["configuration"]["hardware"]["robot_arm"]["ip_address"]
        enable_synchronous_mode = configuration["configuration"]["hardware"]["robot_arm"]["enable_synchronous_mode"]
        import mecademicpy.robot as mdr
        robot = mdr.Robot()
        robot.Connect(address=robot_ip_address, enable_synchronous_mode=enable_synchronous_mode)
        return robot

    elif robot_type.lower() == "syntheticrobot" or robot_type.lower() == "synthetic":
        return DummyDeviceConnection()

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
        print("loaded real module")
        return robot_arm.RobotArm(device_connection=device_connection)
    elif device_type == "synthetic":
        synthetic_device = load_module_from_file(
            "synthetic_device",
            os.path.join(Path(__file__).resolve().parent, "synthetic_device.py"),
        )
        print("loaded synthetic module")
        return synthetic_device.SyntheticRobotArm(device_connection=device_connection)
    else:
        return device_not_found(microscope_name, device_type)
