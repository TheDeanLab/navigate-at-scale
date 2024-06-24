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


class SyntheticRobotArm:
    """A synthetic robot arm for testing purposes"""

    def __init__(self, device_connection, *args):
        """Initialize the Synthetic Device

        Parameters
        ----------
        device_connection : object
            The device connection object
        args : list
            The arguments for the device
        """
        pass

    def jog(self):
        """Zero the joints of the synthetic device"""
        print("*** Synthetic motor receive command: jog")

    def disconnect(self):
        """Disconnects the Mecademic Robot object from the robot and system"""
        print("*** Synthetic robot receive command: disconnect")

    def move_joints(self, a, b, c, d, e, f):
        """Move Robot Joints.

        Parameters
        ----------
        a
        b
        c
        d
        e
        f
        """
        print("*** Synthetic robot receive command: move_joints")

    def move_pose(self, a, b, c, d, e, f):
        """Move Robot Linearly"""
        print("*** Synthetic robot receive command: disconnect")

    def delay(self, wait):
        """Makes the Robot wait"""
        print("*** Synthetic robot receive command: disconnect")

    def activate_and_home(self):
        """Activates and Homes the Robot"""
        print("*** Synthetic robot receive command: disconnect")

    @property
    def commands(self):
        """Return the commands for the synthetic device

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {
            "jog": lambda *args: self.jog(),
        }
