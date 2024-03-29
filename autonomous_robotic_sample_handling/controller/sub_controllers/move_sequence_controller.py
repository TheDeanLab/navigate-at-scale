import tkinter as tk
from tkinter import ACTIVE, DISABLED, filedialog, messagebox

class MoveSequenceController:
    def __init__(self, view, parent_controller=None):
        self.parent_controller = parent_controller
        self.view = view
        
        self.buttons = self.view.buttons 
        self.buttons["stop"].bind("<Button-1>", lambda event: self.handle_click(event, "stop"))
        self.buttons["sample_carousel"].bind("<Button-1>", lambda event: self.handle_click(event, "sample_carousel"))
        self.buttons["sample_microscope"].bind("<Button-1>", lambda event: self.handle_click(event, "sample_microscope"))

        # self.buttons["stop"].bind("<Double-Button-1>", lambda event: self.handle_click(event, "stop"))
        # self.buttons["sample_carousel"].bind("<Double-Button-1>", lambda event: self.handle_click(event, "sample_carousel"))
        # self.buttons["sample_microscope"].bind("<Double-Button-1>", lambda event: self.handle_click(event, "sample_microscope"))
    
        # for button in self.buttons:
            # self.buttons[button].bind("<Button-1>", lambda event: self.handle_click(event, button))

    def handle_click(self, event, buttons):
        print(self.buttons[buttons]['state'])
        print(self.buttons[buttons]['state'] == "normal")
        if self.buttons[buttons]['state']=="normal" or self.buttons[buttons]['state'] == "active":
            print(buttons)
        self.buttons[buttons].configure(state=DISABLED)
        self.view.after(1000, lambda *args: self.buttons[buttons].configure(state=ACTIVE))
