class SyntheticRobotArm:
    def __init__(self, device_connection, *args):
        """ Initialize the Synthetic Device

        Parameters
        ----------
        device_connection : object
            The device connection object
        args : list
            The arguments for the device
        """
        pass

    def zero_joints(self):
        """ Zero the joints of the synthetic device """
        print("*** Synthetic robot receive command: zero joints")

    def disconnect(self):
        """ Disconnects the Mecademic Robot object from the robot and system"""
        print("*** Synthetic robot receive command: disconnect")

    def move_joints(self, a, b, c, d, e, f):
        """ Move Robot Joints """
        print("*** Synthetic robot receive command: move_joints")

    def move_pose(self, a, b, c, d, e, f):
        """ Move Robot Linearly """
        print("*** Synthetic robot receive command: disconnect")

    def delay(self, wait):
        """ Makes the Robot wait """
        print("*** Synthetic robot receive command: disconnect")

    def activate_and_home(self):
        """ Activates and Homes the Robot """
        print("*** Synthetic robot receive command: disconnect")

    @property
    def commands(self):
        """Return the commands for the synthetic device

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {
            "zero_joints": lambda *args: print(
                f"zero robot arm joints!"
            ),
            "disconnect": lambda *args: print(
                f"zero robot arm joints!"
            ),
            "move_joints": lambda *args: print(
                f"move robot arm joint 1 to {args[0]}!"
            ),
            "move_pose": lambda *args: print(
                f"move robot arm to pose x to {args[0]}!"
            ),
            "delay": lambda *args: print(
                f"delay robot actions by {args[0]} seconds!"
            ),
            "activate_and_home": lambda *args: print(
                f"activate and home robot!"
            ),
        }
