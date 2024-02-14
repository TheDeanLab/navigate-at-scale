# Standard Library Imports

# Third Party Imports

# Local Imports
from autonomous_robotic_sample_handling.view.autonomous_robotic_sample_handling_frame import (
    AutonomousRoboticSampleHandlingFrame
)
from autonomous_robotic_sample_handling.controller.sub_controllers.robot_arm_controller import (
    RobotArmController
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

        # Initialize sub-controllers
        self.robot_arm_controller = RobotArmController(
            parent_controller=self
        )

    def move_robot_arm_to_loading_zone(self):
        self.robot_arm_controller.move_joints(0, 0, 45, 0, -45, 0)
        self.robot_arm_controller.move_lin_rel_wrf(100, 0, -50, 0, 0, 0)
        print("Moving robot arm to loading zone")



