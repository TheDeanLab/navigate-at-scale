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
import logging
import tkinter as tk

# Third Party Imports

# Local Imports
from navigate.view.custom_widgets.popup import PopUp

# Logging Setup
p = __name__.split(".")[1]
logger = logging.getLogger(p)


class InHouseToolsPopup(tk.Frame):
    """Popup for in house tools."""

    def __init__(self, root, *args, **kwargs):
        """Initialize the popup.

        Parameters
        ----------
        root : object
            GUI root
        *args : object
            Arguments
        **kwargs : object
            Keyword arguments
        """
        #: PopUp: Popup object
        self.popup = PopUp(
            root,
            "In House Tools",
            "630x420+330+330",
            top=False,
            transient=False,
        )
        # Storing the content frame of the popup, this will be the parent of the widgets
        content_frame = self.popup.get_frame()

        # Formatting
        tk.Grid.columnconfigure(content_frame, "all", weight=1)
        tk.Grid.rowconfigure(content_frame, "all", weight=1)

        #: dict: Buttons for the popup
        self.buttons = {
            "input": tk.Text(content_frame, height=1, width=5),
            "height": tk.Text(content_frame, height=1, width=5),
            "connect": tk.Button(content_frame, text="Connect Robot"),
            "disconnect": tk.Button(content_frame, text="Disconnect Robot"),
            "home": tk.Button(content_frame, text="Home Robot and Motor"),
            "zero": tk.Button(content_frame, text="Zero Joints"),
            "opengripper": tk.Button(content_frame, text="Open Gripper"),
            "closegripper": tk.Button(content_frame, text="Close Gripper"),
            "movetoloadingzone": tk.Button(
                content_frame, text="Move Stage to Initial Loading Zone"
            ),
        }

        counter = 0
        for key, button in self.buttons.items():
            if counter == 0:
                row, column = 0, 0
            elif counter == 1:
                row, column = 0, 1
            elif counter == 3:
                row, column = 0, 2
            elif counter == 4:
                row, column = 1, 0
            elif counter == 5:
                row, column = 1, 1
            elif counter == 6:
                row, column = 1, 2
            elif counter == 7:
                row, column = 2, 0
            elif counter == 8:
                row, column = 2, 1
            elif counter == 9:
                row, column = 2, 2

            button.grid(
                row=row, column=column, sticky=tk.NSEW, padx=(4, 1), pady=(4, 6)
            )
            counter += 1

    def get_buttons(self):
        """Get the buttons for the popup.

        Returns
        -------
        dict
            Buttons for the popup
        """
        return self.buttons
