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
