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

    def move(self, robot):
        """Move the custom device"""
        print("Custom device is going to zero joints")
        robot.MoveJoints(0, 0, 0, 0, 0, 0)
        robot.Delay(15)
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
