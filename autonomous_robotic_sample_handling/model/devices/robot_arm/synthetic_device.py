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

    def move(self, robot):
        """ Move the Synthetic Robot Arm

        Parameters
        ----------
        robot : Mecademicpy.Robot
            The robot object representing the Meca500 robot arm.
        """
        print("*** Synthetic Device receive command: move")

    @property
    def commands(self):
        """Return the commands for the synthetic device

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {
            "move_robot_arm": lambda *args: print(
                f"move synthetic robot arm {args[0]}!"
            )
        }
