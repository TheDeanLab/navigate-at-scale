import mecademicpy.robot as mdr

def connect_to_robot_arm(configuration):
    """ Connect to the Meca500 Robot Arm

    Parameters
    ----------
    configuration

    Returns
    -------

    """
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
    def __init__(self, device_connection: mdr.Robot, *args):
        """ Initialize the Custom Device

        Parameters
        ----------
        device_connection : mdr.Robot
            The device connection object, representing the Meca500 Robot Arm using mecademicpy
        args : list
            The arguments for the device
        """
        self.robot = device_connection

    def zero_joints(self):
        """ Zero all the joints

        Returns
        -------

        """
        print("Custom device is going to zero joints")
        self.robot.MoveJoints(0, 0, 0, 0, 0, 0)
        print('Robot has completed movement')

    def disconnect(self):
        """ Disconnect the robot

        Returns
        -------

        """
        self.robot.Disconnect()
        print("Robot has disconnected")

    def move_joints(self, a, b, c, d, e, f):
        """ Move Joints

        Parameters
        ----------
        a
        b
        c
        d
        e
        f

        Returns
        -------

        """
        self.robot.MoveJoints(a, b, c, d, e, f)

    def move_pose(self, a, b, c, d, e, f):
        """ Move the Robot Arm to a given Pose

        Parameters
        ----------
        a
        b
        c
        d
        e
        f

        Returns
        -------

        """
        self.robot.MovePose(a, b, c, d, e, f)

    def move_lin_rel_wrf(self, x, y, z, alpha, beta, gamma):
        """ Move Robot Linearly with respect to the World Reference Frame

        Parameters
        ----------
        x
        y
        z
        alpha
        beta
        gamma

        Returns
        -------

        """
        self.robot.MoveLinRelWrf(x, y, z, alpha, beta, gamma)

    def delay(self, wait):
        """ Delay the robot operation

        Parameters
        ----------
        wait : int
            time in seconds to delay robot operation
        Returns
        -------

        """
        self.robot.Delay(wait)

    def activate_and_home(self):
        """ Activates and Homes the Robot

        Returns
        -------

        """
        self.robot.ActivateAndHome()

    def load_robot_config(self, config):
        """ Import and apply robot configuration data and limits

        Parameters
        ----------
        config

        Returns
        -------

        """
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
