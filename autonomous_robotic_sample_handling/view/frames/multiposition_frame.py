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

# Third Party Imports
import pandas as pd
from pandastable import Table

# Local Imports


class MultiPositionTab(tk.Frame):
    """MultiPositionTab

    MultiPositionTab is a tab in the main window that allows the user to
    create and run multipoint experiments."""

    def __init__(self, setting_notebook, *args, **kwargs):
        """Initialize the MultiPositionTab

        Parameters
        ----------
        setting_notebook : ttk.Notebook
            The notebook that contains the settings tab.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.
        """
        # Init Frame
        tk.Frame.__init__(self, setting_notebook, *args, **kwargs)

        #: int: The index of the tab in the notebook
        self.index = 3

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        #: MultiPointFrame: The frame that contains the widgets for the multipoint
        # experiment settings.
        self.tiling_buttons = MultiPointFrame(self)
        self.tiling_buttons.grid(
            row=0, column=0, columnspan=3, sticky=tk.NSEW, padx=10, pady=10
        )

        #: MultiPointList: The frame that contains the widgets for the multipoint
        # experiment settings.
        self.multipoint_list = MultiPointList(self)
        self.multipoint_list.grid(
            row=1, column=0, columnspan=3, sticky=tk.NSEW, padx=10, pady=10
        )


class MultiPointFrame(ttk.Labelframe):
    """MultiPointFrame

    MultiPointFrame is a frame that contains the widgets for the multipoint
    experiment settings."""

    def __init__(self, settings_tab, *args, **kwargs):
        """Initialize the MultiPointFrame

        Parameters
        ----------
        settings_tab : tk.Frame
            The frame that contains the settings tab.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.

        """
        text_label = "Multi-Position Acquisition"
        ttk.Labelframe.__init__(self, settings_tab, text=text_label, *args, **kwargs)


class MultiPositionTable(Table):
    """MultiPositionTable

    MultiPositionTable is a class that inherits from Table. It is used to
    customize the table for the multipoint table.
    """

    def __init__(self, parent=None, **kwargs):
        """Initialize the MultiPositionTable

        Parameters
        ----------
        parent : tk.Frame
            The frame that contains the settings tab.
        **kwargs : dict
            Arbitrary keyword arguments.
        """

        super().__init__(parent, width=400, height=500, columns=4, **kwargs)

        self.loadCSV = None
        self.exportCSV = None
        self.insertRow = None
        self.generatePositions = None
        self.addStagePosition = None


class MultiPointList(ttk.Frame):
    """MultiPointList

    MultiPointList is a frame that contains the widgets for the multipoint
    experiment settings. uses Pandastable for embedding an interactive list within a
    tk Frame. https://pandastable.readthedocs.io/en/latest/
    """

    def __init__(self, settings_tab, *args, **kwargs):
        """Initialize the MultiPointList

        Parameters
        ----------
        settings_tab : tk.Frame
            The frame that contains the settings tab.
        *args : tuple
            Variable length argument list.
        **kwargs : dict
            Arbitrary keyword arguments.
        """
        ttk.Frame.__init__(self, settings_tab, *args, **kwargs)

        df = pd.DataFrame(
            {"X": [0], "Y": [0], "Z": [0], "θ1": [0], "θ2": [0], "θ3": [0]}
        )
        #: MultiPositionTable: The PandasTable instance that is being used.
        self.pt = MultiPositionTable(self, showtoolbar=False)
        self.pt.show()
        self.pt.model.df = df

    def get_table(self):
        """Returns a reference to multipoint table dataframe.

        Parameters
        ----------
        self : object
            Multipoint List instance

        Returns
        -------
        self.pt.model.df: Pandas DataFrame
            Reference to table data as dataframe
        """
        return self.pt


class MultipositionButtons(tk.Frame):
    """frame that contains buttons for multiposition table"""

    def __init__(self, settings_tab, *args, **kwargs):
        text_label = "Multiposition Buttons"
        ttk.Labelframe.__init__(self, settings_tab, text=text_label, *args, **kwargs)
        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        # Initializing Button
        self.buttons = {
            "import": ttk.Button(self, text="Load Positions from Disk"),
            "add row": ttk.Button(self, text="Add row"),
            "export": ttk.Button(self, text="Export Position Data"),
            "add stage": ttk.Button(self, text="Add stage position"),
        }

        counter = 0
        for key, button in self.buttons.items():
            if counter == 0:
                row, column = 0, 0
            elif counter == 1:
                row, column = 0, 1
            elif counter == 2:
                row, column = 1, 0
            elif counter == 3:
                row, column = 1, 1

            button.grid(
                row=row, column=column, sticky=tk.NSEW, padx=(4, 1), pady=(4, 6)
            )
            counter += 1
