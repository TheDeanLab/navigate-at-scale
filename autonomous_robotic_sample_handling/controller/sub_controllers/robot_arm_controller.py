class RobotArmController:
    def __init__(self, view, parent_controller=None):
        """ Initialize the Robot Arm Controller

        Parameters
        ----------
        view : object
            The Custom Device View object
        parent_controller : object
            The parent (e.g., main) controller object
        """
        self.view = view
        self.parent_controller = parent_controller

    def MoveToLoadingZone(self, position = 302.3, view=None):
        """

        Parameters
        ----------
        position

        Returns
        -------

        """
        def func(position=position, *args):
            if view is not None:
                text_input = view.buttons["input"].get(1.0, "end-1c")
                if text_input.strip() != "":
                    position = text_input
                else:
                    position = position
            self.parent_controller.execute(
                "moveTo", float(position)
            )
        return func

    def zero_joints(self):
        """

        Returns
        -------

        """
        print("**** Zeroing joints ****")
        self.parent_controller.execute(
            "zero_joints"
        )

    def move_pose(self, a, b, c, d, e, f):
        self.parent_controller.execute(
            "move_pose", a, b, c, d, e, f
        )

    def move_joints(self, a, b, c, d, e, f):
        self.parent_controller.execute(
            "move_joints", a, b, c, d, e, f
        )
    
    def move_lin(self, a, b, c, d, e, f):
        self.parent_controller.execute(
            "move_lin", a, b, c, d, e, f
        )
        
    def open_gripper(self):
        self.parent_controller.execute(
            "open_gripper"
        )
        
    def close_gripper(self):
        self.parent_controller.execute(
            "close_gripper"
        )

    def disconnect(self):
        self.parent_controller.execute(
            "disconnect"
        )
        
    def move_lin_rel_trf(self,a,b,c,d,e,f):
        self.parent_controller.execute(
            "move_lin_rel_trf", a, b, c, d, e, f
        )

    def delay(self,time):
        self.parent_controller.execute(
            "delay", time
        )
    # def move_joints(self, a, b, c, d, e, f):
    #     self.robot_arm.move_joints(a, b, c, d, e, f)
    #     print("Robot has finished moving [move_joints]")
    #
    # def move_pose(self, a, b, c, d, e, f):
    #     self.robot_arm.move_pose(a, b, c, d, e, f)
    #     print("Robot has finished moving [move_pose]")
    #
    # def move_lin_rel_wrf(self, x, y, z, alpha, beta, gamma):
    #     self.robot_arm.move_lin_rel_wrf(x, y, z, alpha, beta, gamma)
    #     print("Robot has finished moving [lin_rel_wrf]")

    def bind_button_events(self, view):
        view.buttons["zero"].configure(command=self.zero_joints)
        view.buttons["disconnect"].configure(command=self.disconnect)
        view.buttons['opengripper'].configure(command=self.open_gripper)
        view.buttons['closegripper'].configure(command=self.close_gripper)
        view.buttons['movetoloadingzone'].configure(command=self.MoveToLoadingZone(view=view))
