
# Standard Library Imports
import tkinter as tk

# Third Party Imports

# Local Imports
from autonomous_robotic_sample_handling.controller.autonomous_robotic_sample_handling_controller import (
AutonomousRoboticSampleHandlingController
)


def main():
    """ For launching the plugin as a standalone application."""
    root = tk.Tk()
    root.title("Autonomous Robotic Sample Handling")
    AutonomousRoboticSampleHandlingController(root=root)
    root.mainloop()


if __name__ == "__main__":
    main()
