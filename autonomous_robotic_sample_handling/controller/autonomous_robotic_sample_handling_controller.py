#from robot_arm_controller import RobotArmController


class AutonomousRoboticSampleHandlingController:
    def __init__(self, view, parent_controller=None):
        self.view = view
        self.parent_controller = parent_controller

        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        # Initialize sub-controllers
        #self.robot_arm_controller = RobotArmController(view, self)
