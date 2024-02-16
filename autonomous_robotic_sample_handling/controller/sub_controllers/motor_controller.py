from autonomous_robotic_sample_handling.model.devices.motor.motor import *

class MotorController:
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
        # self.variables = self.view.get_variables()
        # self.buttons = self.view.buttons
        # self.buttons["zero"].configure(command=self.zero_joints)
        # self.buttons["disconnect"].configure(command=self.disconnect)
        # self.buttons["move"].configure(command=lambda: self.move_joints(0, 0, 0, 0, 90, 0))

        # Manually set up a device connection to the robot arm and initialize the Model
        self.motor = Motor()

    def home(self):
        # self.parent_controller.execute(
        #     "home"
        # )
        self.motor.home()
        print("Home Rotary Stage Motor")
        
    def getPosition(self):
        
        return self.motor.getPosition

    def disconnect(self):
        # self.parent_controller.execute(
        #     "disconnect"
        # )
        self.motor.disconnect()
        print("Stage has disconnected")

    def MoveJog(self,position):
        
        # self.parent_controller.execute(
        #     "MoveJog"
        # )
        
        self.motor.MoveJog(position)
        print("Motor has finished Move Jog")
        

