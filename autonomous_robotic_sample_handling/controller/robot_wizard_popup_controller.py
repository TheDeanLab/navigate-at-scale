# Copyright (c) 2021-2022  The University of Texas Southwestern Medical Center.
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
#

# Standard Library Imports
import logging
import tkinter as tk

# Third Party Imports

# Local Imports
from navigate.tools.multipos_table_tools import (
    sign,
    compute_tiles_from_bounding_box,
    calc_num_tiles,
    update_table,
)
from navigate.controller.sub_controllers.gui_controller import GUIController
from navigate.tools.common_functions import combine_funcs

# Logger Setup
p = __name__.split(".")[1]
logger = logging.getLogger(p)


class TilingWizardController(GUIController):
    """Tiling Wizard Controller

    Controller for tiling wizard parameters.
    Gathers the FOV from the camera settings tab and will
    update when user changes this value.
    Set start/end position buttons will grab the stage
    values for the respective axis when pressed and display in popup
    Number of images we need to acquire with our desired
    percent overlap is calculated and then displayed in third column
    """

    def __init__(self, view, parent_controller):
        """Initialize Tiling Wizard Controller

        Parameters
        ----------
        view : object
            GUI element containing widgets and variables to control.
            Likely tk.Toplevel-derived. In this case tiling_wizard_popup.py
        parent_controller : channels_tab_controller
            The controller that creates the popup/this controller.

        """
        super().__init__(view, parent_controller)

    def showup(self):
        """Show the tiling wizard

        Brings popup window to front of screen

        Examples
        --------
        >>> self.showup()
        """
        self.view.popup.deiconify()
        self.view.popup.attributes("-topmost", 1)
