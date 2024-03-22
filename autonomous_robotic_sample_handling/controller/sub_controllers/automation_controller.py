import tkinter as tk
from tkinter import filedialog, messagebox

class AutomationController:
    def __init__(self, view, parent_controller=None):
        self.parent_controller = parent_controller
        self.view = view

        self.widgets = self.view.get_widgets()
        self.buttons = self.view.buttons

        # #################################
        # ##### Example Widget Events #####
        # #################################

        self.widgets['num_samples'].set("1")
        #TODO: Configure all widgets to be loaded using configuration file data

    def pause_motion(self):
        self.parent_controller.execute(
            "pause_motion"
        )

    def resume_motion(self):
        self.parent_controller.execute(
            "resume_motion"
        )

    def get_num_samples(self):
        return int(self.widgets['num_samples'].get())