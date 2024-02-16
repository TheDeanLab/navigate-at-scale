from autonomous_robotic_sample_handling.model.devices.robot_arm.robot_arm import *

class RobotArmController:
    def __init__(self, parent_controller=None):
        """ Initialize the Robot Arm Controller

        Parameters
        ----------
        parent_controller : object
            The parent (e.g., main) controller object
        """
        super().__init__()

        # Initialize attributes
        self.parent_controller = parent_controller
        self.view = self.parent_controller.view

        # Get the variables and buttons from the view
        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons
        self.buttons["zero"].configure(command=self.zero_joints)
        self.buttons["disconnect"].configure(command=self.disconnect)
        self.buttons["move"].configure(command=lambda: self.move_joints(0, 0, 0, 0, 90, 0))

        # Manually set up a device connection to the robot arm and initialize the Model
        device_robot = connect_to_robot_arm(None)
        self.robot_arm = RobotArm(device_robot)

    def zero_joints(self):
        # self.parent_controller.execute(
        #     "zero_joints"
        # )
        self.robot_arm.zero_joints()
        print("Controller set all robot joints to zero")

    def disconnect(self):
        # self.parent_controller.execute(
        #     "disconnect"
        # )
        self.robot_arm.disconnect()
        print("Controller has disconnected robot")
        
    def move_lin(self,a,b,c,d,e,f):
        self.robot_arm.move_lin(a,b,c,d,e,f)

    def move_joints(self, a, b, c, d, e, f):
        self.robot_arm.move_joints(a, b, c, d, e, f)
        print("Robot has finished moving [move_joints]")

    def move_pose(self, a, b, c, d, e, f):
        self.robot_arm.move_pose(a, b, c, d, e, f)
        print("Robot has finished moving [move_pose]")

    def move_lin_rel_wrf(self, x, y, z, alpha, beta, gamma):
        self.robot_arm.move_lin_rel_wrf(x, y, z, alpha, beta, gamma)
        print("Robot has finished moving [lin_rel_wrf]")

