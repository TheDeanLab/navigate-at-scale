# Standard Imports
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import pandas as pd
from pandastable import Table, Menu, RowHeader, ColumnHeader
from navigate.controller.sub_controllers.gui_controller import GUIController

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

        self.root = root
        self.root.title("Autonomous Robotic Sample Handling")
        self.root.resizable(True, True)
        self.root.geometry("")

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

        # Robot Initialization Buttons
        self.robot_init = RobotInitialization(self)
        self.robot_init.grid(
            row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=10, pady=10
        )
        self.buttons.update(RobotInitialization.get_buttons(self.robot_init))

        # Quick Command Buttons
        self.move_sequence = MoveSequence(self)
        self.move_sequence.grid(
            row=5, column=0, columnspan=2, sticky=tk.NSEW, padx=10, pady=10
        )
        self.buttons.update(MoveSequence.get_buttons(self.move_sequence))

        # Pause and Play Buttons
        self.pause_play = PausePlay(self)
        self.pause_play.grid(
            row=0, column=3, columnspan=2, sticky=tk.NSEW, padx=10, pady=10
        )
        self.buttons.update(PausePlay.get_buttons(self.pause_play))

        self.multiposition = MultiPositionTab(self)
        self.multiposition.grid(
            row=15, column=0, columnspan=2, sticky=tk.NSEW, padx=10, pady=10
        )
        # multiposition table Buttons
        self.MultipositionButtons = MultipositionButtons(self)
        self.MultipositionButtons.grid(
            row=10, column=0, columnspan=2, sticky=tk.NSEW, padx=10, pady=10
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


class RobotInitialization(ttk.Frame):
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
        print("Robot Initialization Frame Created!")

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        # Initializing Button
        self.buttons = {
            "import": ttk.Button(self, text="Load Positions from Disk"),
            "connect": ttk.Button(self, text="Connect Robot"),
            "disconnect": ttk.Button(self, text="Disconnect Robot"),
            "move": ttk.Button(self,text='Move Robot'),
            "zero": ttk.Button(self, text="Zero Joints")
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
            elif counter == 4:
                row, column = 2, 0

            button.grid(
                row=row, column=column, sticky=tk.NSEW, padx=(4, 1), pady=(4, 6)
            )
            counter += 1

    def get_buttons(self):
        return self.buttons


class MoveSequence(ttk.Frame):
    """MoveSequence

    MoveSequence is a frame that contains the widgets for initializing
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
        text_label = 'Quick Commands'
        ttk.Labelframe.__init__(self, settings_tab, text=text_label, *args, **kwargs)

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        # Initializing Button
        self.buttons = {
            "stop": ttk.Button(self, text="STOP"),
            "sample_carousel": ttk.Button(self, text="Sample to carousel"),
            "sample_microscope": ttk.Button(self, text="Sample to microscope"),
        }
        counter = 0
        for key, button in self.buttons.items():
            if counter == 0:
                row, column = 0, 0
            elif counter == 1:
                row, column = 0, 1
            elif counter == 2:
                row, column = 0, 2

            button.grid(
                row=row, column=column, sticky=tk.NSEW, padx=(4, 1), pady=(4, 6)
            )
            counter += 1

    def get_buttons(self):
        return self.buttons


class PausePlay(ttk.Frame):
    """PausePlay

    PausePlay is a frame that contains the widgets for pausing and resuming
    robot actions.

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
        ttk.Labelframe.__init__(self, settings_tab, *args, **kwargs)

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        #Path to pause and play buttons
        image_directory = Path(__file__).resolve().parent
        self.pause_image = tk.PhotoImage(
            file=image_directory.joinpath("images", "pause.png")
        ).subsample(32,32)
        self.play_image = tk.PhotoImage(
            file=image_directory.joinpath("images", "play.png")
        ).subsample(32,32)

        self.buttons = {
            "pause": tk.Button(self, image=self.pause_image, borderwidth=0),
            "play": tk.Button(self, image=self.play_image, borderwidth=0),
        }

        # Gridding out Buttons
        self.buttons['play'].grid(
            row=0, column=0, rowspan=1, columnspan=1, padx=2, pady=2
        )
        self.buttons['pause'].grid(
            row=0, column=2, rowspan=1, columnspan=1, padx=2, pady=2
        )

    def get_buttons(self):
        return self.buttons
    

class MultiPositionTab(tk.Frame):
    """MultiPositionTab

    MultiPositionTab is a tab in the main window that allows the user to
    create and run multipoint experiments."""

    def __init__(self, setntbk, *args, **kwargs):
        """Initialize the MultiPositionTab

        Parameters
        ----------
        setntbk : ttk.Notebook
            The notebook that contains the settings tab.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.
        """
        # Init Frame
        tk.Frame.__init__(self, setntbk, *args, **kwargs)

        #: The index of the tab in the notebook
        self.index = 3

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        #: MultiPointFrame: The frame that contains the widgets for the multipoint
        # experiment settings.
        self.tiling_buttons = MultiPointFrame(self)
        self.tiling_buttons.grid(
            row=0, column=0, columnspan=3, sticky=tk.NSEW, padx=10, pady=10
        )

        #: MultiPointList: The frame that contains the widgets for the multipoint
        # experiment settings.
        self.multipoint_list = MultiPointList(self)
        self.multipoint_list.grid(
            row=1, column=0, columnspan=3, sticky=tk.NSEW, padx=10, pady=10
        )
class MultiPointFrame(ttk.Labelframe):
    """MultiPointFrame

    MultiPointFrame is a frame that contains the widgets for the multipoint
    experiment settings."""

    def __init__(self, settings_tab, *args, **kwargs):
        """Initialize the MultiPointFrame

        Parameters
        ----------
        settings_tab : tk.Frame
            The frame that contains the settings tab.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.

        """
        text_label = "Multi-Position Acquisition"
        ttk.Labelframe.__init__(self, settings_tab, text=text_label, *args, **kwargs)
        
        #pd.options.display.max_rows = 9999
        #position_data = pd.read_csv(r"C:\Users\jocam\Desktop\BMEN 4388\code\position_data.csv")
        #print(position_data)

class MultiPositionTable(Table):
    """MultiPositionTable

    MultiPositionTable is a class that inherits from Table. It is used to
    customize the table for the multipoint table.
    """

    def __init__(self, parent=None, **kwargs):
        """Initialize the MultiPositionTable

        Parameters
        ----------
        parent : tk.Frame
            The frame that contains the settings tab.
        **kwargs : dict
            Arbitrary keyword arguments.
        """

        super().__init__(parent, width=400, height=500, columns=4, **kwargs)

        self.loadCSV = None
        self.exportCSV = None
        self.insertRow = None
        self.generatePositions = None
        self.addStagePosition = None

        #position_data = pd.read_csv("desktop/BMEN 4388/code/position_data.csv")
        #position_data.head()
        

class MultiPointList(ttk.Frame):
    """MultiPointList

    MultiPointList is a frame that contains the widgets for the multipoint
    experiment settings. uses Pandastable for embedding an interactive list within a
    tk Frame. https://pandastable.readthedocs.io/en/latest/
    """

    def __init__(self, settings_tab, *args, **kwargs):
        """Initialize the MultiPointList

        Parameters
        ----------
        settings_tab : tk.Frame
            The frame that contains the settings tab.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.
        """
        ttk.Frame.__init__(self, settings_tab, *args, **kwargs)

        df = pd.DataFrame({"X": [0], "Y": [0], "Z": [0], "θ1": [0], "θ2": [0], "θ3": [0]})
        #: MultiPositionTable: The PandasTable instance that is being used.
        self.pt = MultiPositionTable(self, showtoolbar=False)
        self.pt.show()
        self.pt.model.df = df

    def get_table(self):
        """Returns a reference to multipoint table dataframe.

        Parameters
        ----------
        self : object
            Multipoint List instance

        Returns
        -------
        self.pt.model.df: Pandas DataFrame
            Reference to table data as dataframe
        """
        return self.pt
    

class MultipositionButtons(tk.Frame):
    """frame that contains buttons for multiposition table"""
    def __init__(self, settings_tab, *args, **kwargs):
        text_label = 'Multiposition Buttons'
        ttk.Labelframe.__init__(self, settings_tab, text=text_label, *args, **kwargs)
        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        # Initializing Button
        self.buttons = {
            "import": ttk.Button(self, text="Load Positions from Disk"),
            "add row": ttk.Button(self, text="Add row"),
            "export": ttk.Button(self, text="Export Position Data"),
            "add stage": ttk.Button(self,text='Add stage position')
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