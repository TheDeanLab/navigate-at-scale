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
        self.buttons["movetoloadingzone"].configure(command=self.MoveToLoadingZone)

    def test_connection(self):
        self.parent_controller.execute(
            "jog"
        )

    def home(self):
        self.parent_controller.execute(
            "home"
        )
        print("Homing Rotary Stage Motor")
    
    def MoveTo(self, position):
        self.parent_controller.execute(
            "moveTo", position
        )
    
    def MoveToLoadingZone(self, position = 263):
        self.parent_controller.execute(
            "moveTo", position
        )
        
    def getPosition(self):
        
        return self.parent_controller.execute(
            "position"
        )

    def disconnect(self):
        self.parent_controller.execute(
            "disconnect"
        )
        print("Stage has disconnected")

    def MoveJog(self,position):
        
        self.parent_controller.execute(
            "moveJog", position
        )
        print("Motor has finished Move Jog")
        

