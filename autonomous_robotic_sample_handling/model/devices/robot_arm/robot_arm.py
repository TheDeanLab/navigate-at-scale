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
    # device.Disconnect()
    # print("Device disconnected")

class RobotArm:
    """A Robot Arm class"""
    def __init__(self, device_connection: mdr.Robot, *args):
        """ Initialize the Custom Device

        Parameters
        ----------
        device_connection : object
            The device connection object
        args : list
            The arguments for the device
        """
        self.robot = device_connection

    def zero_joints(self):
        """Zero the joints"""
        print("Custom device is going to zero joints")
        self.robot.MoveJoints(0, 0, 0, 0, 0, 0)
        print('Robot has completed movement')

    def disconnect(self):
        self.robot.Disconnect()
        print("Robot has disconnected")

    def move_joints(self, a, b, c, d, e, f):
        """Move Robot Joints"""
        self.robot.MoveJoints(a, b, c, d, e, f)

    def move_pose(self, a, b, c, d, e, f):
        """Move Robot Linearly"""
        self.robot.MovePose(a, b, c, d, e, f)

    def delay(self, wait):
        """Makes the Robot wait"""
        self.robot.Delay(wait)

    def activate_and_home(self):
        """Activates and Homes the Robot"""
        self.robot.ActivateAndHome()

    def load_robot_config(self):
        """Imports limits defined in the yaml file. Needs to be called before ActivateAndHome"""
        self.robot.SetJointLimits()
        self.robot.SetTorqueLimits()

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {
            "zero_joints": lambda *args: self.zero_joints(),
            "disconnect": lambda *args: self.disconnect(),
        }
