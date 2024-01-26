# Standard Imports
import os
from pathlib import Path

# Third party imports
import mecademicpy.robot as mdr
from tkinter import messagebox

# Local application imports
from navigate.tools.common_functions import load_module_from_file
from navigate.model.device_startup_functions import device_not_found

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
    """Build device connection.

    Returns
    -------
    device_connection : object
    """
    with mdr.Robot() as robot:
        try:
            robot.Connect(address='192.168.0.100')
            print('Robot has connected')
            #print("Homing the robot")
            #robot.Home()
            #print("Waiting until the robot is homed.")
            #robot.WaitHomed()
            #print("Moving robot to a start position")
            #robot.MoveJoints(0, 0, 45, 0, -45, 0)
            #print("Activating the robot")
            #robot.ActivateRobot()
            #print("Homing the robot")
            #robot.Home()
        except:
            messagebox.showerror("Error", "The robot could not connect")
    return type("DeviceConnection", (object,), {})


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

    """Start device.

    Returns
    -------
    device_object : object
    """
    if is_synthetic:
        device_type = "synthetic"
    else:
        device_type = configuration["configuration"]["microscopes"][microscope_name][
            "robot_arm"
        ]["hardware"]["type"]

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
        return synthetic_device.SyntheticDevice(device_connection=device_connection)
    else:
        return device_not_found(microscope_name, device_type)
