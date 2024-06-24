# Copyright (c) 2021-2024  The University of Texas Southwestern Medical Center.
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted for academic and research use only
# (subject to the limitations in the disclaimer below)
# provided that the following conditions are met:

#      * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.

#      * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.

#      * Neither the name of the copyright holders nor the names of its
#      contributors may be used to endorse or promote products derived from this
#      software without specific prior written permission.

# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


# Standard Library Imports
import tkinter as tk
from tkinter import ttk

# Third-Party Imports

# Local Imports
from navigate.view.custom_widgets.LabelInputWidgetFactory import LabelInput
from navigate.view.custom_widgets.validation import ValidatedSpinbox
from autonomous_robotic_sample_handling.view.popups.inhouse_tools_popup import (
    InHouseToolsPopup,
)


class MoveSequence(tk.Frame):
    """MoveSequence

    MoveSequence is a frame that contains the widgets for initializing
    robot movement.
    """

    def __init__(self, settings_tab, *args, **kwargs):

        """Initialize MoveSequence Frame

                Parameters
        ----------
        settings_tab : tk.Frame
            The frame that contains the settings tab.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.
        """
        text_label = "Move Sequence"
        ttk.Labelframe.__init__(self, settings_tab, text=text_label, *args, **kwargs)

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        #: dict: Dictionary of buttons in the frame.
        self.buttons = {
            "offline_program": ttk.Button(self, text="Start program"),
            "automation_sequence": ttk.Button(self, text="Start automation sequence"),
            "process_sample": ttk.Button(self, text="Process a sample"),
            "in_house": ttk.Button(self, text="In House Tools"),
            "import": ttk.Button(self, text="Load Positions from Disk"),
        }
        counter = 0
        for key, button in self.buttons.items():
            if counter == 0:
                row, column = 0, 0
            elif counter == 1:
                row, column = 0, 1
            elif counter == 2:
                row, column = 0, 2
            elif counter == 3:
                row, column = 1, 1
            elif counter == 4:
                row, column = 1, 2

            button.grid(
                row=row, column=column, sticky=tk.NSEW, padx=(4, 1), pady=(4, 6)
            )
            counter += 1

        #: dict: Dictionary of variables in the frame.
        self.variables = {
            "current_sample_id": tk.IntVar(self, 0),
            "progress_bar_style": ttk.Style(),
            # TODO: Consider benefits of specifying a number_of_samples variable for
            #  the num_samples LabelInput
        }

        self.in_house_tools = InHouseToolsPopup(self)
        self.buttons.update(InHouseToolsPopup.get_buttons(self.in_house_tools))

        # Define styles for widgets
        self.variables["progress_bar_style"].layout(
            "text.Horizontal.TProgressbar",
            [
                (
                    "Horizontal.Progressbar.trough",
                    {
                        "children": [
                            (
                                "Horizontal.Progressbar.pbar",
                                {"side": "left", "sticky": "ns"},
                            )
                        ],
                        "sticky": "nswe",
                    },
                ),
                ("Horizontal.Progressbar.label", {"sticky": ""}),
            ],
        )

        #: dict: Dictionary of widgets in the frame.
        self.inputs = {
            "num_samples": LabelInput(
                parent=self,
                label="Number of samples",
                input_class=ValidatedSpinbox,
                input_var=tk.IntVar(),
                input_args={"from_": 1, "to": 24, "increment": 1, "width": 5},
            ),
            "automation_progress": ttk.Progressbar(
                self,
                orient=tk.HORIZONTAL,
                mode="determinate",
                length=200,
                variable=self.variables["current_sample_id"],
                maximum=24,
                style="text.Horizontal.TProgressbar",
            ),
        }
        self.inputs["num_samples"].grid(row=1, column=0, padx=(4, 1), pady=(4, 6))
        self.inputs["automation_progress"].grid(
            row=2, column=0, padx=(4, 1), pady=(4, 6)
        )

    def get_buttons(self):
        """Get Buttons.

        This function returns the dictionary that holds the buttons.

        Returns
        -------
        dict
            Dictionary of all the buttons in the frame.
        """
        return self.buttons

    def get_widgets(self):
        """Get Widgets.

        This function returns the dictionary that holds the widgets.

        The key is the widget name, value is the LabelInput class that has all the data.

        Returns
        -------
        dict
            Dictionary of all the widgets in the frame.
        """
        return self.inputs

    def get_variables(self):
        """Get Variables.

        This function returns the dictionary that holds the variables.

        Returns
        -------
        dict
            Dictionary of all the variables in the frame.
        """

        return self.variables
