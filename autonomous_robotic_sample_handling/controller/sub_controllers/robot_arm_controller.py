

class RobotArmController:
    def __init__(self, parent_controller=None):
        """ Initialize the Robot Arm Controller

        Parameters
        ----------
        parent_controller : object
            The parent (e.g., main) controller object
        """
        super().__init__()

        # Initialize attributes
        self.parent_controller = parent_controller
        self.view = self.parent_controller.view

        # Get the variables and buttons from the view
        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons
        self.buttons["zero"].configure(command=self.zero_joints)

    def zero_joints(self):
        # self.parent_controller.execute(
        #     "zero_joints"
        # )
        print("Zeroing joints")