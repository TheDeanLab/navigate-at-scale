import mecademicpy.robot as mdr

def connect_to_robot_arm(configuration):
    robot = mdr.Robot()
    print("Attempting connection")
    robot.Connect(address='192.168.0.100', enable_synchronous_mode=True)
    start_robot_arm(robot, None)
    return robot

def start_robot_arm(device: mdr.Robot, configuration):
    print("Activating and Homing robot arm")
    device.Move
    device.ActivateAndHome()
    device.Delay(2)
    device.Disconnect()

class RobotArm:
    """A Robot Arm class"""
    def __init__(self, device_connection, *args):
        """ Initialize the Custom Device

        Parameters
        ----------
        device_connection : object
            The device connection object
        args : list
            The arguments for the device
        """
        self.device_connection = device_connection

    def zero_joints(self, robot):
        """Zero the joints"""
        print("Custom device is going to zero joints")
        robot.MoveJoints(0, 0, 0, 0, 0, 0)
        print('Robot has completed movement')

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {"move_robot_arm": lambda *args: self.move(args[0])}
