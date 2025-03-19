from decimal import Decimal
class SyntheticRobotArm:
    """ A synthetic robot arm for testing purposes """
    def __init__(self, device_connection, *args):
        """ Initialize the Synthetic Device

        Parameters
        ----------
        device_connection : object
            The device connection object
        args : list
            The arguments for the device
        """
        self.position = 0

    def home(self):
        """Home the motor"""
        print("Homing Synthetic Motor")

    def MoveJog(self, MotorDirection):
        """Move the motor in the specified direction.

        Parameters
        ----------
        MotorDirection : str
            The direction to move the motor in
        """
         #Pass string or initialize MotorDirection.Forward/Backward outside?
         
        print(f"Synthetic motor moves jog in {MotorDirection}")
            
    def setHomingVelocity(self, velocity):
        print(f"Set Synthetic motor homing velocity: {velocity}")

    def MoveTo(self, Position):
        """Move the motor to the specified position.

        Parameters
        ----------
        Position : int
            The position to move the motor to
        """
        self.position = Decimal(Position)
        print(f"Moving Synthetic motor to position {Decimal(Position)}")

    def disconnect(self):
        """Disconnect the motor"""
        print("Disconnect from Synthetic motor!")
        
    def getPosition(self):
        """Get the motor position.

        Returns
        -------
        int
            The motor position
        """
        return self.position
    
    def SetJogStepSize(self, JogStepSize):
        """Set the jog step size.

        Parameters
        ----------
        JogStepSize : int
            The jog step size
        """
        print(f"Set Synthetic motor jog step size: {Decimal(JogStepSize)}")
        
    def SetJogVelocityParams(self, JogVelocity,JogAccel):
        """Set the jog velocity parameters.

        Parameters
        ----------
        JogVelocity : int
            The jog velocity
        """
        print(f"Set Synthetic motor jog velocity params: {Decimal(JogVelocity)}, {Decimal(JogAccel)}")

    @property
    def commands(self):
        """Return the commands for the synthetic device

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {
            "home": lambda *args: self.home(),
            "disconnect": lambda *args: self.disconnect(),
            "moveJog": lambda *args: self.MoveJog(args[0]),
            "position": lambda *args: self.getPosition(),
            "moveTo": lambda *args: self.MoveTo(args[0]),
            "setHomingVelocity": lambda *args: self.setHomingVelocity(args[0])
        }
