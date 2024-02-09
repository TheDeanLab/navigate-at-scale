#from autonomous_robotic_sample_handling.model.devices.robot_arm.robot_arm import RobotArm
#from autonomous_robotic_sample_handling.view.popups.robot_wizard_popup import RobotWizardPopup

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
        self.buttons["connect"].configure(command=self.connect_robot)
        self.buttons["launch"].configure(command=self.launch_robot_wizard)

    def launch_robot_wizard(self):
        """Launches tiling wizard popup.

        Will only launch when button in GUI is pressed, and will not duplicate.
        Pressing button again brings popup to top

        Examples
        --------
        >>> self.launch_tiling_wizard()
        """

        if hasattr(self, "robot_wizard_controller"):
            self.robot_wizard_controller.showup()
            return
        robot_wizard = RobotWizardPopup(self.view)
        self.robot_wizard_controller = RobotWizardController(robot_wizard, self)

    def zero_joints(self):
            print("Test zero joints") 

    def connect_robot(self):
        RobotArm.ActivateAndHome()