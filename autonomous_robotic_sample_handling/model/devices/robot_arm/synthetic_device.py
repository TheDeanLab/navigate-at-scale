class SyntheticRobotArm:
    """ A synthetic robot arm class """
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

    def start_program(self, program_name):
        """ Start offline robot program

        Parameters
        ----------
        program_name : str
            String containing the offline program name

        Returns
        -------

        """
        print(f"*** Synthetic robot receive command: Start {program_name} program")

    def zero_joints(self):
        """ Zero the joints of the synthetic device

        Returns
        -------

        """
        print("*** Synthetic robot receive command: zero joints")

    def disconnect(self):
        """ Disconnects the Mecademic Robot object from the robot and system

        Returns
        -------

        """
        print("*** Synthetic robot receive command: disconnect")

    def move_joints(self, a, b, c, d, e, f):
        """ Move Robot Joints """
        print("*** Synthetic robot receive command: move_joints")

    def move_pose(self, a, b, c, d, e, f):
        """ Move Robot Linearly """
        print("*** Synthetic robot receive command: disconnect")

    def delay(self, wait):
        """ Delays robot operation by a specified time

        Parameters
        ----------
        wait : float
            time in seconds to delay the robot

        Returns
        -------

        """
        print(f"*** Synthetic robot receive command: delay by {wait} seconds")

    def activate_and_home(self):
        """ Activates and Homes the Robot

        Returns
        -------

        """
        print("*** Synthetic robot receive command: activate and home")

    def pause_robot_motion(self):
        """ Pause robot motion for synthetic device

        Returns
        -------

        """
        print("*** Synthetic robot receive command: pause robot motion")

    def resume_robot_motion(self):
        """ Resume robot motion for synthetic device

        Returns
        -------

        """
        print("*** Synthetic robot receive command: resume robot motion")

    def reset_robot_motion(self):
        """ Reset robot motion for synthetic device

        Returns
        -------

        """
        print("*** Synthetic robot receive command: reset robot motion")

    def reset_error(self):
        """ Reset robot error for synthetic device

        Returns
        -------

        """
        print("*** Synthetic device received command: reset error")

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
            "pause_motion": lambda *args: self.pause_robot_motion(),
            "resume_motion": lambda *args: self.resume_robot_motion(),
            "reset_motion": lambda *args: self.reset_robot_motion(),
            "start_program": lambda *args: self.start_program(args[0]),
            "reset_error": lambda *args: self.reset_error()
        }
