import mecademicpy.robot as mdr

class RobotArm:
    """A Robot Arm class"""
    def __init__(self, device_connection: mdr.Robot, *args):
        """ Initialize the Custom Device

        RobotArm(device_connection, arg1, arg2)

        Parameters
        ----------
        device_connection : object
            The device connection object
        args : list
            The arguments for the device
        """
        self.robot = device_connection

    def MovetoZero(self):
        """Move the custom device"""
        print("Custom device is going to zero joints")
        self.robot.MoveJoints(0, 0, 0, 0, 0, 0)
        print('Robot has completed movement')

    def Disconnect(self):
        """Disconnect the robot"""
        self.robot.Disconnect()
        print("Robot has disconnected")

    def MoveJoints(self, a, b, c, d, e, f):
        """Move Robot Joints"""
        self.robot.MoveJoints(a,b,c,d,e,f)

    def MovePose(self, a, b, c, d, e, f):
        """Move Robot Linearly"""
        self.robot.MovePose(a,b,c,d,e,f)

    def Delay(self, wait):
        """Makes the Robot wait"""
        self.robot.Delay(wait)

    def ActivateAndHome(self):
        """Activates and Homes the Robot"""
        self.robot.ActivateAndHome()

    

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {"move_robot_arm": lambda *args: self.move(args[0])}
