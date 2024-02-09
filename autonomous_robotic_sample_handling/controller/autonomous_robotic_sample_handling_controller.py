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

        # Initialize sub-controllers
        self.robot_arm_controller = RobotArmController(
            parent_controller=self
        )

    def zero_joints(self):
        self.robot_arm_controller.zero_joints()

