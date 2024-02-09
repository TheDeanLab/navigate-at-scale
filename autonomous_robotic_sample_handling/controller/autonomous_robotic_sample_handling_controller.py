from autonomous_robotic_sample_handling.controller.sub_controllers import (
    RobotArmController
)
class AutonomousRoboticSampleHandlingController:
    def __init__(self, view, parent_controller=None):
        self.view = view
        self.parent_controller = parent_controller

        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons
        # print(self.buttons)

        # Initialize sub-controllers
        # self.robot_arm_controller = RobotArmController(self.view, self.parent_controller)

        self.buttons["zero"].configure(command=self.zero_joints)

    def zero_joints(self):
        self.parent_controller.execute(
            "zero_joints"
        )
