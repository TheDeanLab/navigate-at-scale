Connect to the MecaPortal: http://192.168.0.100/

Remove the E-Stop.

Reset the stage from the remote controller.

Activate and home. YOu can leave the browser open to monitor the device, but
you must put it in the monitoring mode...

Installed the plugin

When you launch, you should see the in house tools GUI

..image:: images/in_house_tools.PNG

The tab too...

..image:: images/custom_tab.PNG

Tuning.

Usually done in MecaPortal.
manual_tuning.rst...

Process a sample - grabs a sample, moves it to the microscope, releases it,
grabs it, and goes back to the carousel. Does not move the carousel, assumes
it is already in the proper location.

Start automation sequence - does process a sample in a loop, for the number
of samples specified.

Start program - Runs an offline program (e.g., one saved in the MecaPortal).
Currently hard-coded to run Vertical_Oscillation.

Multiposition table - Not implemented.

Load positions from disk. Pretty pointless without the table, and duplicated.

The in house tools button throws errors


