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
        super().__init__(view, parent_controller)

        # Get the variables and buttons from the view
        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        self.buttons["zero"].configure(command=self.zero_joints)

        def zero_joints(self):
            print("Test zero joints")