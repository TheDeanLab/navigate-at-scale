import tkinter as tk
from tkinter import ttk
from pathlib import Path


class PausePlay(tk.Frame):
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
        image_directory = Path(__file__).resolve().parent.parent
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
