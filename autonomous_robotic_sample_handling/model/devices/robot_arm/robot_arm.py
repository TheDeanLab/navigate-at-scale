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

# Third Party Imports
import mecademicpy.robot as mdr

# Local Imports


class RobotArm:
    """Robot Arm class"""

    def __init__(self, device_connection: mdr.Robot, *args):
        """Initialize the Custom Device

        RobotArm(device_connection, arg1, arg2)

        Parameters
        ----------
        device_connection : mdr.Robot
            The device connection object, representing the Meca500 Robot Arm using
            mecademicpy
        args : list
            The arguments for the device
        """

        #: mdr.Robot: The robot arm object
        self.robot = device_connection

        # TODO: Split Activation() and Home(), as configuration may need to be
        #  done before homing and after activation
        self.robot.ActivateAndHome()
        self.zero_joints()  # Zero robot arm joints on start
        self.robot.SetJointVelLimit(30)
        self.robot.SetTorqueLimitsCfg(4, 0)
        self.robot.SetTorqueLimits(40.0, 60.0, 40.0, 40.0, 40.0, 40.0)

    def start_program(self, program_name):
        """Start offline robot program

        Parameters
        ----------
        program_name : str
            String containing the offline program name
        """
        self.robot.StartProgram(program_name)

    def disconnect(self):
        """Disconnect the robot arm"""
        self.robot.Disconnect()

    def zero_joints(self):
        """Zero all robot arm joints"""
        self.robot.MoveJoints(0, 0, 0, 0, 0, 0)

    def move_joints(self, j1, j2, j3, j4, j5, j6):
        """Move robot arm joints to the specified angles

        Parameters
        ----------
        j1 : float
            Angle of joint 1
        j2 : float
            Angle of joint 2
        j3 : float
            Angle of joint 3
        j4 : float
            Angle of joint 4
        j5 : float
            Angle of joint 5
        j6 : float
            Angle of joint 6
        """
        self.robot.MoveJoints(j1, j2, j3, j4, j5, j6)

    def move_lin(self, x, y, z, rx, ry, rz):
        """Move the robot arm along a linear path (in Cartesian space) to a given pose

        Parameters
        ----------
        x : float
            position in x
        y : float
            position in y
        z : float
            position in z
        rx : float
            angle around x-axis
        ry : float
            angle around y-axis
        rz : float
            angle around z-axis

        """
        self.robot.MoveLin(x, y, z, rx, ry, rz)

    def move_lin_rel_trf(self, x, y, z, rx, ry, rz):
        """Move robot arm relative to the tool reference frame

        Parameters
        ----------
        x : float
            distance (mm) in x
        y : float
            distance (mm) in y
        z : float
            distance (mm) in z
        rx : float
            angle around x-axis
        ry : float
            angle around y-axis
        rz : float
            angle around z-axis
        """
        self.robot.MoveLinRelTrf(x, y, z, rx, ry, rz)

    def move_lin_rel_wrf(self, x, y, z, rx, ry, rz):
        """Move Robot Linearly with respect to the World Reference Frame

        Parameters
        ----------
        x : float
            distance (mm) in x
        y : float
            distance (mm) in y
        z : float
            distance (mm) in z
        rx : float
            angle around x-axis
        ry : float
            angle around y-axis
        rz : float
            angle around z-axis
        """
        self.robot.MoveLinRelWrf(x, y, z, rx, ry, rz)

    def move_pose(self, x, y, z, rx, ry, rz):
        """Move Robot Arm to the given Pose

        Parameters
        ----------
        x : float
            position in x
        y : float
            position in y
        z : float
            position in z
        rx : float
            angle around x-axis
        ry : float
            angle around y-axis
        rz : float
            angle around z-axis
        """
        self.robot.MovePose(x, y, z, rx, ry, rz)

    def delay(self, wait):
        """Delays robot operation by a specified time

        Parameters
        ----------
        wait : float
            time in seconds to delay the robot
        """
        self.robot.Delay(wait)

    def activate_and_home(self):
        """Activate and Home the robot arm"""
        self.robot.ActivateAndHome()

    def load_robot_config(self, config=None):
        """Apply robot operation limits from configuration data

        Parameters
        ----------
        config : yaml
            User-defined data for robot arm operating limits and configuration

        """
        # Apply joint velocity limits
        self.robot.SetJointVelLimit(30)

        # Apply torque limits
        # TODO: Modify to use proper data type
        self.robot.SetTorqueLimitsCfg(4, 0)
        self.robot.SetTorqueLimits(40.0, 60.0, 40.0, 40.0, 40.0, 40.0)

    def open_gripper(self):
        """Open robot arm gripper"""
        self.robot.GripperOpen()

    def close_gripper(self):
        """Close robot arm gripper"""
        self.robot.GripperClose()

    def pause_robot_motion(self):
        """Pause motion of the robot arm"""
        self.robot.PauseMotion()

    def resume_robot_motion(self):
        """Resume motion of the robot arm"""
        self.robot.ResumeMotion()

    def reset_robot_motion(self):
        """Reset motion queue for the robot arm"""
        self.robot.ClearMotion()

    def reset_error(self):
        """Reset robot error."""
        self.robot.ResetError()
        # TODO: Add functionality to return to standby position, or employ recovery mode
        # (avoid obstacles and work zone, zero_joints, etc.)

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {
            "start_program": lambda *args: self.start_program(args[0]),
            "disconnect": lambda *args: self.disconnect(),
            "zero_joints": lambda *args: self.zero_joints(),
            "move_joints": lambda *args: self.move_joints(
                args[0], args[1], args[2], args[3], args[4], args[5]
            ),
            "move_lin": lambda *args: self.move_lin(
                args[0], args[1], args[2], args[3], args[4], args[5]
            ),
            "move_lin_rel_trf": lambda *args: self.move_lin_rel_trf(
                args[0], args[1], args[2], args[3], args[4], args[5]
            ),
            "move_lin_rel_wrf": lambda *args: self.move_lin_rel_wrf(
                args[0], args[1], args[2], args[3], args[4], args[5]
            ),
            "move_pose": lambda *args: self.move_pose(
                args[0], args[1], args[2], args[3], args[4], args[5]
            ),
            "delay": lambda *args: self.delay(args[0]),
            "open_gripper": lambda *args: self.open_gripper(),
            "close_gripper": lambda *args: self.close_gripper(),
            "pause_motion": lambda *args: self.pause_robot_motion(),
            "resume_motion": lambda *args: self.resume_robot_motion(),
            "reset_motion": lambda *args: self.reset_robot_motion(),
            "reset_error": lambda *args: self.reset_error(),
        }
