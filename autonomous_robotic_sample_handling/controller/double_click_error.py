#imports
import tkinter
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter import messagebox

#imports for frame and controllers
from autonomous_robotic_sample_handling.controller import autonomous_robotic_sample_handling_controller  
from autonomous_robotic_sample_handling.view.autonomous_robotic_sample_handling_frame import AutonomousRoboticSampleHandlingFrame, MoveSequence


class autonomous_robotic_sample(autonomous_robotic_sample_handling_controller):

    def double_click(self,event):
        buttonclicked = AutonomousRoboticSampleHandlingFrame.MoveSequence.sample_carousel(event)
        buttonclicked = AutonomousRoboticSampleHandlingFrame.MoveSequence.sample_microscope(event)
        tkinter.messagebox.showinfo("Error: button double clicked.")
        self.autonomous_robotic_sample_handling_controller.execute("stop")
        