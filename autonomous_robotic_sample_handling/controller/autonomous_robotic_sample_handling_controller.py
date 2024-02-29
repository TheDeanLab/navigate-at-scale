from autonomous_robotic_sample_handling.controller.sub_controllers import (
    RobotArmController
)

from autonomous_robotic_sample_handling.controller.sub_controllers.multiposition_controller import (
    MultipositionController
)

class AutonomousRoboticSampleHandlingController:
    def __init__(self, view, parent_controller=None):
        self.view = view
        self.parent_controller = parent_controller

        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        self.buttons['sample_carousel'].configure(command=self.move_robot_arm_to_loading_zone)

        # Initialize sub-controllers
        self.robot_arm_controller = RobotArmController(
            self.view, self.parent_controller
        )
        self.multiposition_controller = MultipositionController(
            parent_controller=self
        )


    def move_robot_arm_to_loading_zone(self):
        self.robot_arm_controller.move_joints(0, 0, 45, 0, -45, 0)
        self.robot_arm_controller.move_lin_rel_wrf(100, 0, -50, 0, 0, 0)
        print("Moving robot arm to loading zone")



