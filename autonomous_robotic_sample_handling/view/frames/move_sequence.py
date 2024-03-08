import tkinter as tk
from tkinter import ttk


class MoveSequence(tk.Frame):
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
        text_label = 'Move Sequence'
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
