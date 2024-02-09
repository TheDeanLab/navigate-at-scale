#from autonomous_robotic_sample_handling.controller.robot_arm_controller import RobotArmController
#from autonomous_robotic_sample_handling.view.popups.robot_wizard_popup import RobotWizardPopup

class AutonomousRoboticSampleHandlingController:
    def __init__(self, view, parent_controller=None):
        self.view = view
        self.parent_controller = parent_controller
        
        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons
    
    