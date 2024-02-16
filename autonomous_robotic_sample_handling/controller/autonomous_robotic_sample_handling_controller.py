# Standard Library Imports

# Third Party Imports

# Local Imports
from autonomous_robotic_sample_handling.view.autonomous_robotic_sample_handling_frame import (
    AutonomousRoboticSampleHandlingFrame
)
from autonomous_robotic_sample_handling.controller.sub_controllers.robot_arm_controller import (
    RobotArmController
)

from autonomous_robotic_sample_handling.controller.sub_controllers.motor_controller import (
    MotorController
)

class AutonomousRoboticSampleHandlingController:
    def __init__(self,
                 root,
                 ):
        """ Initialize the Autonomous Robotic Sample Handling Controller

        Parameters
        ----------
        root : object
            The root object (e.g., the Tkinter root object)
        """

        # Initialize attributes
        self.root = root
        self.view = AutonomousRoboticSampleHandlingFrame(root)
        self.view.pack(expand=True, fill="both")

        # Get the variables and buttons from the view
        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        self.buttons['sample_carousel'].configure(command=self.move_robot_arm_to_loading_zone)

        self.buttons['sample_microscope'].configure(command=self.mainLoop)

        #Initialize sub-controllers
        self.robot_arm_controller = RobotArmController(
            parent_controller=self
        )

        self.motor_controller = MotorController(
            parent_controller=self
        )
        
    def move_robot_arm_to_loading_zone(self):
        self.robot_arm_controller.move_lin(263.89, 24.28, 159.23, 0, 90, 0)
        self.robot_arm_controller.zero_joints()
        #self.robot_arm_controller.move_joints(263.89, 24.28, 159.23, 0, 90, 0)
        #self.robot_arm_controller.move_lin_rel_wrf(100, 0, -50, 0, 0, 0)
        print("Moving robot arm to loading zone")
        
    def CycleStage(self):
        self.motor_controller.MoveJog("Forward")
        
    def mainLoop(self):
        print("cycling")
        while True:
            self.move_robot_arm_to_loading_zone()
            self.CycleStage()
        
    



