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

        self.buttons['sample_microscope'].configure(command=self.cycle)
      

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
        
        #change inputs to refer to config file
        self.robot_arm_controller.move_lin(275, -1.5, 141.5, 0, 90, 0)
        print("Moving robot arm to loading zone")
        
    def engageHeader(self):
        
        self.robot_arm_controller.open_gripper()
        self.robot_arm_controller.move_lin_rel_trf(0,0,46,0,0,0)
        self.robot_arm_controller.delay(1)
        self.robot_arm_controller.close_gripper()
    
    def removeHeaderFromStage(self):
        self.robot_arm_controller.move_lin_rel_trf(-40,0,0,0,0,0)
    
    def moveToMicroscope(self):
        self.robot_arm_controller.move_lin(133,-250,190,90,0,-90)
    
    def engageMicroscope(self):
        self.robot_arm_controller.move_lin_rel_trf(0,0,40,0,0,0)
        self.robot_arm_controller.move_lin_rel_trf(-10,0,0,0,0,0)
        self.robot_arm_controller.open_gripper()
    
    def disengageMicroscope(self):
        self.robot_arm_controller.move_lin_rel_trf(0,0,-100,0,0,0)
    
    def removeHeaderFromMicroscope(self):
        self.robot_arm_controller.move_lin_rel_trf(-10,0,40,0,0,0)
        self.robot_arm_controller.close_gripper()
        self.robot_arm_controller.delay(1)
        self.robot_arm_controller.move_lin_rel_trf(0,-50,0,0,0,0)
        self.robot_arm_controller.move_lin_rel_trf(0,0,-100,0,0,0)
        
    def returnHeaderToCarousel(self):
        #TODO: var_height = 10 is for the chamfered header, var_height = 0 is 0 for regular [cleanup later]
        var_height = 10
        input = self.buttons["height"].get(1.0, "end-1c")
        non_empty_text = input == ""
        if not non_empty_text:
            var_height = float(input)
        
        self.robot_arm_controller.move_lin(275,-1.5,150+var_height,0,90,0)
        self.robot_arm_controller.delay(.5)
        self.robot_arm_controller.move_lin_rel_trf(0,0,37.8,0,0,0)
        self.robot_arm_controller.delay(.5)
        self.robot_arm_controller.move_lin_rel_trf(9+var_height,0,0,0,0,0)
        self.robot_arm_controller.open_gripper()
        self.robot_arm_controller.move_lin_rel_trf(0,0,-40,0,0,0)
        
    def CycleStage(self):
        self.motor_controller.MoveJog("Forward")
        print("Test motor cycle stage")

    def cycle(self):
        print("cycling")
        
        self.motor_controller.MoveToLoadingZone()
        
        self.move_robot_arm_to_loading_zone()
        self.engageHeader()
        self.removeHeaderFromStage()
        self.moveToMicroscope()
        self.engageMicroscope()
        self.disengageMicroscope()
        
        self.moveToMicroscope()
        self.removeHeaderFromMicroscope()
        self.returnHeaderToCarousel()
