# Standard Library Imports
import logging
import tkinter as tk
from tkinter import ttk

# Third Party Imports

# Local Imports
from navigate.view.custom_widgets.popup import PopUp

# Logging Setup
p = __name__.split(".")[1]
logger = logging.getLogger(p)


class InHouseToolsPopup(tk.Frame):
    """Popup for in house tools

    Parameters
    ----------
    root : object
        GUI root
    *args : object
        Arguments
    **kwargs : object
        Keyword arguments

    Attributes
    ----------
    popup : object
        Popup window
    inputs : dict
        Dictionary of inputs
    buttons : dict
        Dictionary of buttons

    Methods
    -------
    get_variables()
        Returns the variables
    get_buttons()
        Returns the buttons
    get_widgets()
        Returns the widgets

    """

    def __init__(self, root, *args, **kwargs):
        self.popup = PopUp(
            root,
            "In House Tools",
            "630x420+330+330",
            top=False,
            transient=False,
        )
        # Storing the content frame of the popup, this will be the parent of
        # the widgets
        content_frame = self.popup.get_frame()
        content_frame.columnconfigure(0, pad=5)
        content_frame.columnconfigure(1, pad=5)
        content_frame.rowconfigure(0, pad=5)
        content_frame.rowconfigure(1, pad=5)
        content_frame.rowconfigure(2, pad=5)

        # Formatting
        tk.Grid.columnconfigure(content_frame, "all", weight=1)
        tk.Grid.rowconfigure(content_frame, "all", weight=1)

        # Initializing Button
        self.buttons = {
            "input": tk.Text(content_frame, height=1, width=5),
            "height": tk.Text(content_frame, height=1, width=5),
        }

        # Label
        self.labels = {
            "input": tk.Label(content_frame, text="Move motor"),
            "height": tk.Label(content_frame, text="Change robot height at drop")
        }
        counter = 0
        for key, button in self.buttons.items():
            label = self.labels[key]
            if counter == 0:
                row, column = 0, 0
            elif counter == 1:
                row, column = 0, 1

            label.grid(
                row=row, column=column, sticky=tk.NSEW, padx=(4, 1), pady=(4, 6)
            )
            button.grid(
                row=row+1, column=column, sticky=tk.NSEW, padx=(4, 1), pady=(4, 6)
            )
            counter += 1

    def get_buttons(self):
        return self.buttons