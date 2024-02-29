import mecademicpy.robot as mdr

def connect_to_robot_arm(configuration):
    robot = mdr.Robot()
    print("Attempting connection")
    robot.Connect(address='192.168.0.100', enable_synchronous_mode=True)
    start_robot_arm(robot, None)
    return robot

def start_robot_arm(device: mdr.Robot, configuration):
    print("Activating and Homing robot arm")
    device.ActivateAndHome()
    device.Delay(2)
    device.Disconnect()

class RobotArm:
    """A Robot Arm class for controlling the Meca500 robot arm"""
    def __init__(self, device_connection: mdr.Robot, *args):
        """ Initialize the RobotArm class

        Parameters
        ----------
        device_connection : object
            The device connection object
        args : list
            The arguments for the device
        """

        #: The connection to the Meca500 Robot Arm
        self.robot = device_connection
        self.robot.ActivateAndHome()
        print("*** is robot there?", self.robot)


    def zero_joints(self):
        """Zero the joints"""
        print("Custom device is going to zero joints")
        self.robot.MoveJoints(0, 0, 0, 0, 0, 0)
        print('Robot has completed movement')

    def move_joints(self, *args):
        print("Move robot arm to new position")
        self.robot.MoveJoints(0, 0, 0, 0, 90, 0)
        print('Robot has completed movement')

    def disconnect(self):
        print("Disconnecting robot")
        self.robot.Disconnect()

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {"zero_joints": lambda *args: self.zero_joints(),
                "move_joints": lambda *args: self.move_joints(*args),
                "disconnect": lambda *args: self.disconnect(),
                }
