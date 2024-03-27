import mecademicpy.robot as mdr

class RobotArm:
    """A Robot Arm class"""
    def __init__(self, device_connection: mdr.Robot, *args):
        """ Initialize the Custom Device

        RobotArm(device_connection, arg1, arg2)

        Parameters
        ----------
        device_connection : mdr.Robot
            The device connection object, representing the Meca500 Robot Arm using mecademicpy
        args : list
            The arguments for the device
        """
        self.robot = device_connection
        #TODO: Split Activation() and Home(), as configuration may need to be done before homing and after activation
        self.robot.ActivateAndHome()
        self.zero_joints()
        #self.robot.SetTrf(0,0,0,0,0,0)
        self.robot.SetTorqueLimitsCfg(4, 0)
        self.robot.SetTorqueLimits(30.0,60.0,30.0,30.0,30.0,30.0)
        # self.robot.SetAutoConf(1)
        # self.robot.SetAutoConfTurn(1)

    def pause_robot_motion(self):
        """ Pause robot motion

        Returns
        -------

        """
        print("Pause robot motion")
        self.robot.PauseMotion()

    def resume_robot_motion(self):
        """ Resume robot motion

        Returns
        -------

        """
        print("Resume robot motion")
        self.robot.ResumeMotion()

    def reset_robot_motion(self):
        """ Reset robot operations

        Returns
        -------

        """
        self.robot.ClearMotion()

    def start_program(self, program_name):
        """ Start offline robot program

        Parameters
        ----------
        program_name : str
            String containing the offline program name

        Returns
        -------

        """
        self.robot.StartProgram(program_name)

    def reset_error(self):
        """ Reset robot error

        Returns
        -------

        """
        self.robot.ResetError()
        #TODO: Add functionality to return to standby position
        # (avoid obstacles and work zone, zero_joints, etc.)

    def zero_joints(self):
        """ Zero all the joints

        Returns
        -------

        """
        self.robot.MoveJoints(0, 0, 0, 0, 0, 0)
        print('Robot has zeroed joints')
        
    def move_lin(self,a,b,c,d,e,f):
        """ Moves linearly to an orientation and position relative to the world reference frame

        Returns
        -------

        """
        self.robot.MoveLin(a,b,c,d,e,f)
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
        
    def move_lin_rel_trf(self, a, b, c, d, e, f):
        """ Move joints relative to the tool reference frame

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
        self.robot.MoveLinRelTrf(a, b, c, d, e, f)
    
    def delay(self,time):
        
        """ Move joints relative to the tool reference frame

        Parameters
        ----------
        time

        Returns
        -------

        """
        self.robot.Delay(time)
        

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
        
    def move_lin(self,a,b,c,d,e,f):
        
        self.robot.MoveLin(a,b,c,d,e,f)

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
        
    def open_gripper(self):
        """ Open gripper to maximum setting

        Parameters
        ----------
        config

        Returns
        -------

        """
        self.robot.GripperOpen()
        
    def close_gripper(self):
        """ Close gripper to maximum setting

        Parameters
        ----------
        config

        Returns
        -------

        """
        self.robot.GripperClose()

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {"zero_joints": lambda *args: self.zero_joints(),
                "move_pose": lambda *args: self.move_pose(args[0][0], args[0][1], args[0][2], args[0][3], args[0][4], args[0][5]),
                "move_joints": lambda *args: self.move_joints(args[0][0], args[0][1], args[0][2], args[0][3], args[0][4], args[0][5]),
                # "move_joints": lambda *args: self.move_joints(args[0]),
                "disconnect": lambda *args: self.disconnect(),
                "move_lin_rel_trf": lambda *args: self.move_lin_rel_trf(args[0][0], args[0][1], args[0][2], args[0][3], args[0][4], args[0][5]),
                "move_lin": lambda *args: self.move_lin(args[0][0], args[0][1], args[0][2], args[0][3], args[0][4], args[0][5]),
                "open_gripper": lambda *args: self.open_gripper(),
                "close_gripper": lambda *args: self.close_gripper(),
                "delay": lambda *args: self.delay(args[0][0]),
                "pause_motion": lambda *args: self.pause_robot_motion(),
                "resume_motion": lambda *args: self.resume_robot_motion(),
                "reset_motion": lambda *args: self.reset_robot_motion(),
                "start_program": lambda *args: self.start_program(args[0][0]),
                "reset_error": lambda *args: self.reset_error()
                }
