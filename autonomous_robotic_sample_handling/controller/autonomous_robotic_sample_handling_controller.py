from navigate.tools.file_functions import load_yaml_file

from autonomous_robotic_sample_handling.controller.sub_controllers import (
    RobotArmController
)

from autonomous_robotic_sample_handling.controller.sub_controllers.multiposition_controller import (
    MultipositionController
)

from autonomous_robotic_sample_handling.controller.sub_controllers.motor_controller import (
    MotorController
)
 

class AutonomousRoboticSampleHandlingController:
    def __init__(self, view, parent_controller=None):
        self.view = view
        self.parent_controller = parent_controller

        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        self.buttons['sample_carousel'].configure(command=self.move_robot_arm_to_loading_zone)

        self.buttons['sample_microscope'].configure(command=self.mainLoop)

        #Initialize sub-controllers
        self.robot_arm_controller = RobotArmController(
            self.view, self.parent_controller
        )
        self.multiposition_controller = MultipositionController(
            self.view, self.parent_controller
        )

        self.motor_controller = MotorController(
            self.view, self.parent_controller
        )
    
    def get_positions(self):
        data = load_yaml_file('C:/Users/abhik/Documents/Senior Design/navigate-at-scale/autonomous_robotic_sample_handling/config/configuration.yaml')
        robot_position = data['environment']['robot']['trf']
        return robot_position

    def move_robot_arm_to_loading_zone(self):
        self.robot_arm_controller.move_joints(0, 0, 45, 0, -45, 0)
        self.robot_arm_controller.move_lin_rel_wrf(100, 0, -50, 0, 0, 0)
        print("Moving robot arm to loading zone")

    def CycleStage(self):
        self.motor_controller.MoveJog("Forward")

    def mainLoop(self):
        print("cycling")
        while True:
            self.move_robot_arm_to_loading_zone()
            self.CycleStage()





