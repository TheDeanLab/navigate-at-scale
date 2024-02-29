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
        # Get the variables and buttons from the view
        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        self.buttons["zero"].configure(command=self.zero_joints)
        self.buttons["move"].configure(command=self.move_joints)
        self.buttons["disconnect"].configure(command=self.disconnect)

    def zero_joints(self):
        self.parent_controller.execute(
            "zero_joints"
        )

    def move_joints(self):
        self.parent_controller.execute(
            "move_joints"
        )

    def disconnect(self):
        self.parent_controller.execute(
            "disconnect"
        )
