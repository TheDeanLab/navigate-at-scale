import tkinter as tk
from tkinter import ttk

from navigate.view.custom_widgets.LabelInputWidgetFactory import LabelInput
from navigate.view.custom_widgets.validation import ValidatedSpinbox, ValidatedEntry


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
            "offline_program": ttk.Button(self, text="Start program"),
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

        self.inputs = {
            "num_samples": LabelInput(
                parent=self,
                label="Number of samples",
                input_class=ValidatedSpinbox,
                input_var=tk.StringVar(),
                input_args={"from_": 1, "to": 24, "increment": 1, "width": 5},
            )
        }
        self.inputs['num_samples'].grid(row=1, column=0, padx=(4, 1), pady=(4, 6))

    def get_buttons(self):
        return self.buttons

    def get_widgets(self):
        """Get Widgets.

        This function returns the dictionary that holds the widgets.

        The key is the widget name, value is the LabelInput class that has all the data.

        Parameters
        ----------
        self.inputs : dict
            Dictionary of all the widgets in the frame.
        """
        return self.inputs
