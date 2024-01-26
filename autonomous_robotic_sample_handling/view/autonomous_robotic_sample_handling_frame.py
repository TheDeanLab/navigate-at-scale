# Standard Imports
import tkinter as tk
from tkinter import ttk


class AutonomousRoboticSampleHandlingFrame(ttk.Frame):
    """Plugin Frame: Just an example

    This frame contains the widgets for the plugin.
    """

    def __init__(self, root, *args, **kwargs):
        """Initialization of the  Frame

        Parameters
        ----------
        root : tkinter.ttk.Frame
            The frame that this frame will be placed in.
        *args
            Variable length argument list.
        **kwargs
            Arbitrary keyword arguments.
        """
        ttk.Frame.__init__(self, root, *args, **kwargs)

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        # Dictionary for widgets and buttons
        #: dict: Dictionary of the widgets in the frame
        self.inputs = {}
        self.buttons = {}
        self.variables = {}

        # #################################
        # ######## Example Widgets ########
        # ##### add your widgets here #####
        # #################################
        label = ttk.Label(self, text="Plugin Name:")
        label.grid(row=0, column=0, sticky=tk.NW)

        self.variables["plugin_name"] = tk.StringVar(self)
        self.inputs["plugin_name"] = ttk.Entry(
            self, textvariable=self.variables["plugin_name"]
        )
        self.inputs["plugin_name"].grid(
            row=0, column=1, sticky="N", padx=5, pady=(0, 5)
        )

        self.buttons["move"] = ttk.Button(self, text="MOVE")
        self.buttons["move"].grid(row=1, column=1, sticky="N", padx=6)

        # Robot Initialization Buttons
        self.robot_init = RobotInitialization(self)
        self.robot_init.grid(
            row=5, column=0, columnspan=2, sticky=tk.NSEW, padx=10, pady=10
        )


    # Getters
    def get_variables(self):
        """Returns a dictionary of the variables for the widgets in this frame.

        The key is the widget name, value is the variable associated.

        Returns
        -------
        variables : dict
            Dictionary of the variables for the widgets in this frame.
        """
        return self.variables

    def get_widgets(self):
        """Returns a dictionary of the widgets in this frame.

        The key is the widget name, value is the LabelInput class that has all the data.

        Returns
        -------
        self.inputs : dict
            Dictionary of the widgets in this frame.
        """
        return self.inputs

class RobotInitialization(tk.Frame):
    """RobotInitialization

    RobotInitialization is a frame that contains the widgets for initializing
    robot movement.

    Parameters
    ----------
    settings_tab : tk.Frame
        The frame that contains the settings tab.
    *args : tuple
        Variable length argument list.
    **kwargs : dict
        Arbitrary keyword arguments.

    Attributes
    ----------
    buttons : dict
        A dictionary of all the buttons that are tied to each widget name.
        The key is the widget name, value is the button associated.

    Methods
    -------
    """
    def __init__(self, settings_tab, *args, **kwargs):
        text_label = 'Robot Initialization'
        ttk.Labelframe.__init__(self, settings_tab, text=text_label, *args, **kwargs)

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        # Initializing Button
        self.buttons = {
            "import": ttk.Button(self, text="Load Positions from Disk"),
            "connect": ttk.Button(self, text="Connect Robot"),
            "export": ttk.Button(self, text="Home Robot"),
            "launch": ttk.Button(self,text='Move Robot')
        }
        counter = 0
        for key, button in self.buttons.items():
            if counter == 0:
                row, column = 0, 0
            elif counter == 1:
                row, column = 0, 1
            elif counter == 2:
                row, column = 1, 0
            elif counter == 3:
                row, column = 1,1

            button.grid(
                row=row, column=column, sticky=tk.NSEW, padx=(4, 1), pady=(4, 6)
            )
            counter += 1