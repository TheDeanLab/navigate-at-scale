from navigate.tools.file_functions import load_yaml_file
from navigate.config.config import get_navigate_path


from autonomous_robotic_sample_handling.controller.sub_controllers.robot_arm_controller import (
    RobotArmController
)

from autonomous_robotic_sample_handling.controller.sub_controllers.multiposition_controller import (
    MultipositionController
)

from autonomous_robotic_sample_handling.controller.sub_controllers.motor_controller import (
    MotorController
)

from autonomous_robotic_sample_handling.controller.sub_controllers.pause_play_controller import (
    PausePlayController
)

from autonomous_robotic_sample_handling.controller.sub_controllers.automation_controller import (
    AutomationController
)

class AutonomousRoboticSampleHandlingController:
    def __init__(self, view, parent_controller=None):
        self.view = view
        self.parent_controller = parent_controller

        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        self.buttons['automation_sequence'].configure(command=self.automated_sample_handling)
        self.buttons['process_sample'].configure(command=self.move_robot_arm_to_loading_zone)
        self.buttons['offline_program'].configure(command=self.start_offline_program)
        
        self.data = self.load_config_data()
        self.motor_position = self.get_motor_position(self.data)

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
        self.pause_play_controller = PausePlayController(
            self.view.pause_play, self.parent_controller
        )
        self.automation_controller = AutomationController(
            self.view.move_sequence, self.parent_controller
        )

    def load_config_data(self):
        import os
        plugins_config_path = os.path.join(
        get_navigate_path(), "config", "plugins_config.yml"
        )
        plugins_config = load_yaml_file(plugins_config_path)
        plugin_path = plugins_config["Autonomous Robotic Sample Handling"] 
        local_config_path = os.path.join(plugin_path, "config", "configuration.yaml")
        data = load_yaml_file(local_config_path)
        return data
    
    def start_offline_program(self):
        self.parent_controller.execute(
            "start_program", "vertical_oscillation"
        )

    def get_motor_position(self, data):
        motor_position = data["environment"]["motor"]["units"]
        motor_to_robot_mm = motor_position*25.4
        #for standard TRF, z is forwards, x is down
        data_points = {
            "robot_base": data["environment"]["robot"]["robot_base_plate_height"],
            "vial_height": data["environment"]["components"]["vial_height_from_carousel"],
            "carousel_height": data["environment"]["components"]["carousel_height_from_table"],
            "vial_attack": data["environment"]["components"]["vial_attack_distance_from_carousel"],
            "wrf_to_trf": data["environment"]["components"]["trf_from_wrf_cartesian"],
            "trf_gripper_edge": data["environment"]["components"]["trf_to_gripper_edge"],
            "trf_gripper_bottom": data["environment"]["components"]["trf_to_gripper_bottom"],
            "MEPG_thickness": data["environment"]["components"]["MEPG_thickness"],
            "tolerance_up": data["environment"]["components"]["tolerance_up"],
            "tolerance_forward": data["environment"]["components"]["tolerance_forward"],
        }
        print(data_points["robot_base"],data_points["wrf_to_trf"][2],data_points["carousel_height"],data_points["vial_height"])
        print(motor_to_robot_mm, data_points["vial_attack"], data_points["wrf_to_trf"][0], data_points['tolerance_forward'], data_points['trf_gripper_edge'])
        motor_position_x = data_points["robot_base"] + data_points["wrf_to_trf"][2] - data_points["carousel_height"] - data_points["vial_height"] - data_points['trf_gripper_bottom'] -data_points['tolerance_up']
        motor_position_z = motor_to_robot_mm - data_points["vial_attack"] - data_points["wrf_to_trf"][0] - data_points['tolerance_forward'] - data_points["MEPG_thickness"]
        print(motor_to_robot_mm - data_points["vial_attack"] - data_points["wrf_to_trf"][0] - data_points['tolerance_forward'] - data_points['trf_gripper_edge'])
        self.key_positions = {
            "motor_position": [motor_position_x, 0, motor_position_z, 0, 0, 0],
            "engage_header_distance": data_points['trf_gripper_edge'] - data_points['MEPG_thickness']
        }
        print(self.key_positions)

    def move_robot_arm_to_loading_zone(self):
        #TODO: change inputs to refer to config file
        goal_pos = self.key_positions['motor_position']
        x, y, z, Rx, Ry, Rz = goal_pos
        z = z - self.key_positions['engage_header_distance']
        self.robot_arm_controller.move_lin_rel_trf(x, y, z, Rx, Ry, Rz)
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

    def sample_iteration(self):
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

        #TODO: Add function to rotate motor to next loading zone

    def automated_sample_handling(self):
        num_samples = self.automation_controller.get_num_samples()
        print(f"Processing {num_samples} samples")
        for i in range(1, num_samples + 1):
            # self.sample_iteration()
            #TODO: Configure to use official sample iteration sequence once complete
            print(f"Finished processing sample {i}")

