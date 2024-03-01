from autonomous_robotic_sample_handling.model.devices.motor.motor import *

class MotorController:
    def __init__(self, view, parent_controller=None):
        """ Initialize the Robot Arm Controller

        Parameters
        ----------
        parent_controller : object
            The parent (e.g., main) controller object
        """

        # Initialize attributes
        self.view = view
        self.parent_controller = parent_controller

        # Get the variables and buttons from the view
        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        self.buttons["import"].configure(command=self.test_connection)

    def test_connection(self):
        self.parent_controller.execute(
            "jog"
        )

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
        

