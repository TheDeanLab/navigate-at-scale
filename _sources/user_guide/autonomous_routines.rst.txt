======================================
Autonomously Generated Routines
======================================

The *navigate-at-scale* program is designed to autonomously generate routines for the required
devices, specifically the robot arm and motor, in order to automate the sample handling process.
These routine-generation procedures operate using critical data about the experiment setup, such
as the loading zone and microscope position in the Cartesian space, design specifications such as
vial height, and other such parameters. This allows for the application of this program to many
reconfigurable environments. Consider if the robot arm or carousel subsystems must be
repositioned or a new microscope or environment has been setup. Simply relocate the critical
loading zones using the robot arm and update the configuration data
accordingly, which can be found in the
``autonomous_robotic_sample_handling/config/configuration.yaml`` file. The
**navigate**
program can continue running as expected.

.. note::
    While the design-based solution is defined and discussed in this section, it has not been
    completed to function for all reconfigurable environments. As the precision of the routines would
    also be dependent on the precision of all measurements associated with the design approach, the
    manual tuning approach was selected as the primary focus of this project.

------------------------------------

Reference Frames
------------------------------------

Tool Reference Frame (TRF). This is relative to the gripper itself. positive
Z is in the direction of the gripper fingers, positive X is downwards, and
positive Y is to the left of the gripper. Euler angle rotations are defined
as Rx, Ry, Rz, where Rx is the rotation about the X-axis, Ry is the rotation
about the Y-axis, and Rz is the rotation about the Z-axis.

World Reference Frame (WRF). This is relative to the robot arm base. Positive Z
is vertical up, X is forward, Y is to the left. Euler angle rotations are
defined as Rx, Ry, Rz, where Rx is the rotation about the X-axis, Ry is the
rotation about the Y-axis, and Rz is the rotation about the Z-axis.

-------------------------------------

The General Routine Procedure
-------------------------------------

To generate routines for the robot arm and other devices, it was required to design a general
routine that all routines would emulate, following some set of operating guidelines. These
operating guidelines are built upon a set of conditions required for safe and efficient operation
of the system. Combined with other operational parameters and environmental conditions,
appropriate control routines can be developed for automated sample handling.

The general routine can be described as follows. A visual of the end-effector path throughout the
first half of the routine is also provided below:

.. image:: images/system_view_front.png
  :alt: Alternative Routines

#. The robot arm homes to the 'zero joints' position.

#. The robot arm moves toward the loading zone of the carousel, positioning itself in front of
   the loading zone by a distance, *engage_header_distance*.

   * This parameter, defined by the length of the gripper fingers plus the thickness of the
     gripper, represents a minimum distance the robot arm should maintain before moving forward
     to grip the header plate.

#. The robot arm moves forward (+z in the tool reference frame, or TRF) by the
   distance *engage_header_distance*.

   * This sequence positions the gripper fingers exactly around the header plate, preparing for
     acquiring the sample.

   * This sequence simply performs a linear motion. The alignment for orientation, height, and
     related positioning all occurs in the previous motion.

#. The robot arm grips the header plate.

   * A strict range for the close_gripper() function has not been devised, as the sensory
     feedback of the gripper has been satisfactory in closing the gripper effectively around the
     target header plater while limiting flex in the gripper fingertips.

   * In the automatic gripper torque mode, a second LED indicates when
     sufficient torque has been detected, indicating the presence of the
     substrate that you are trying to grab. This is located on the side of the
     gripper, and is adjacent to the LED that indicates that the gripper is
     powered on.

#. The robot arm lifts the header plate by a distance *sample_height*.

   * The sample height is a data parameter specified in the configuration.yaml file which
     represents the height of the sample below the header plate. This variable specifies how
     high a selected sample must be lifted in order to prevent collisions with the sample for future
     operations. The sample_height variable is primarily influenced by the length of the threaded
     rod, the sample insert size, and any desired tolerances.

#. The robot arm performs a vertical oscillation maneuver.

   * The vertical oscillation maneuver is a simple drip management technique in place to limit
     the amount of solvent that drips onto the operating environment space.

   * This maneuver is currently performed using sub-routine commands from the robot's offline
     program storage, rather than directly within the plugin software.
     Specifically, the robot is capable of storing routines generated from
     within MecaPortal in its memory. These can then be called and executed
     from Python, as is done here.

   .. Todo::
        Paste the sequence here...

#. The robot arm returns to the 'zero joints' position.

   * This is an intermediate step to reset all robot arm joints and positioning before proceeding
     operations.

#. The robot arm moves toward the microscope loading zone, positioning itself at a distance,
   *engage_header_distance*. The positioning of the robot arm is also lower in the WRF z
   dimension, by a distance *z_tolerance*.

   * The robot positioning is lowered by an additional factor *z_tolerance* here to position the
     held header plate below the opposite magnet fixed to the microscope. It is desirable to
     attach the sample (via the header plate) from the bottom of the microscope fixture. This
     avoids disruption from the magnets and keeps the sample secure until attached to the
     microscope for imaging.

   * The *z_tolerance* is a user-defined feature though it is dependent on the available
     operating space. A distance of 10 mm is currently assumed for this tolerance.

#. The robot moves forward and up, attaching the sample to the microscope.

   * The robot arm moves forward and up by the *engage_header_distance* and *z_tolerance*
     distances respectively.

#. The robot arm retracts backward (w.r.t. to the TRF) by the *engage_header_distance*.

   * The robot arm has now attached the sample and is waiting for the
     microscope to begin imaging the sample.

#. The robot arm moves forward (w.r.t. to the TRF) by the *engage_header_distance* and grips the
   sample.

   * The microscope has now completed imaging the sample and the robot arm prepares to remove the
     sample from the microscope.

#. The robot arm shears the sample off the microscope.

   * In order to remove the magnetically attached sample and header plate, a simple linear motion
     is performed, a clean shear. The force of the gripper and speed of the motion is sufficient
     to leave the microscope untouched and smoothly remove the sample.

#. The robot arm returns to the 'zero joints' position

   * This is an intermediate step to reset all robot arm joints and positioning before proceeding
     operations.

#. The robot arm moves toward the loading zone of the carousel, positioning itself on top of
   the loading zone by a distance, *sample_height*.

   * The robot arm positions the sample and header plate straight above the
     loading zone, aligned to lower it into place. The positioning of the
     header plate a distance of *sample_height* above the loading zone is to
     prevent the sample from colliding with the vials or carousel.

#. The robot arm opens the gripper, releasing the header plate.

#. The robot arm retracts from the loading zone.

Following the completion of a complete routine, the program either:

- terminates, if the last sample has been processed.
- continues with the next sample in queue, should the queue be non-empty.
    - The motor rotates by 15 degree increments to the next sample's loading zone.

-----------------------------

Routine Generation Approaches
-----------------------------

There are two primary approaches to generating autonomous routines for the **navigate**-based
automated sample handling system:

- **Design-Based Approach**:
    The design-based approach is based on geometric calculations of measured data, in which a
    series of measurements related to the desired actions are collected and the corresponding
    sub-routines formed.
- **Manual-Tuning**:
    Alternatively, the critical locations for the experiment, such as the loading zone and the
    microscope staging area, can be identified by manually operating the robot arm using the
    Mecaportal software to the desired poses.

.. warning::
    The design-based approach is currently incomplete, as it only operates with the carousel in
    directly in front of the robot. More detailed subroutines have not been built for the
    microscope staging area interactions either. As such, it is recommended to stick to the
    manual tuning approach for which extensive testing has been with for the system.

--------------

Critical Data
---------------------
All data for the generation of control routines is held within the
``configuration.yaml`` file, located within the plugin under the *config*
directory.

.. note::
    The configuration data for this experiment is retained within this plugin for the isolation of
    this data. **navigate** tools are utilized to locate and acquire this data during operation
    with the larger **navigate** ecosystem. It is considered best practice to directly host these
    configuration files within the *.navigate* directory for future applications.

There are three major categories of critical data collected in the first iteration of this
program. These are discussed in more detail below:

-   The most critical data refers to the robot arm poses for the loading zone and the microscope
    staging area. All routines are based off of these data points where the robot arm performs a
    series of actions.

    - Currently, all locations are devised with reference to the robot arm's center base as the
      origin, to reflect the origin of the robot within Mecaportal. As discussed in the guide to
      manual tuning, the location updated in the ``configuration.yaml`` refers
      to the robot arm's
      end-effector pose when the robot arm is in the desired position. This is the simplest
      strategy as the `MoveLin()` commands that position the robot arm within
      the critical location
      zones all operate on the robot arm's local world reference frame.
    - A feature has been set up to assume a non-zero robot base, should it be of interest to
      define all critical locations with respect to a global origin of the table or such. In such
      a case, simply find the difference between the critical location and the robot base to find
      the required movement of the robot arm within its local reference.
    - There exists a flag in the ``configuration.yaml`` to enforce whether the
      manually tuned loading
      zone data should be used, or if the design-based approach results should be prioritized. It
      is currently set to **true** and should remain as such unless the design-based approach is
      adjusted.
-   The second set of critical data refers to the physical measurements of the system components
    and the environment. Data such as the thickness of the gripper, the length of the
    gripper fingertips, and other such measurements are critical to devise routines that avoid
    collision of the robot arm with the environment or the damaging of any samples.

    - Currently, design related component data is also included within this section. Data such as
      the vial height in the carousel or the carousel radius are required components for the
      design-based approach for routine generation. Note that such data is designed to simplify
      the required geometric calculations and not to focus on the component itself.
-   The final set of of critical data refers to the tunable parameters within this routine
    generation program. This data refers to variables such as the height of the sample, the
    distance to shear the sample, or the initial motor position for the loading zone. These
    values are subject to the user's opinion or are dependent on the specific experiment setup.

--------------

Future Improvements
------------------------------

-   The autonomous routine generation program has been designed to be re-configurable for all
    environments. However some aspects of it require manual adjustment, something that would
    preferably be avoided. This specifically applies to modifications to parameters of the
    `MoveLin()` function calls within the autonomous script, as the remaining
    operations are based
    on the TRF and function irrespective of the robot arm orientation.

    - Consider 'Step 2' where the robot arm positions itself in front of the loading zone. The
      robot arm sends a command `self.robot_arm_controller.move_lin(x - engage_header_distance,
      y, z, Rx, Ry, Rz)`. Here, the carousel is always assumed to be placed in front of the
      robot arm (where x > 0 in the WRF) and for this reason, the *engage_header_distance* value
      must be subtracted from the *x* parameter to safely position the robot. Otherwise, the
      robot arm would crash into the carousel. This becomes more prominent with the positioning
      of the microscope, traditionally placed in the left or right planes of the robot arm (y < 0
      or y > 0 in the WRF) and both the shear direction must be adjusted to avoid selecting a
      position that would put the robot arm in error.
      Currently, this must be handled by the user directly, who would use their own understanding
      of the environment and orientation to determine a suitable direction and distance to shear the
      sample off the microscope staging area. An update to this system would utilize the relative
      orientation and pose of the robot arm and accordingly determine a suitable shear direction.
      An additional flag or parameter could override this if necessary.
-   Some parameters are currently hard-coded into the system and have not been updated after the
    testing phases. Update these in the prepare_config_data() and configuration setup. Determine
    suitable parameters of interest that could be of use for setting up experiments.
-   The use of intermediate checkpoints have been used to return the robot arm to a safe position
    and limit the possibility of the robot entering an error state. Intermediate checkpoints can
    also be used to enforce specific motions or avoid obstacles. Suppose the microscope staging area
    is in a position only reachable by the robot arm in one particular pose. A set of
    intermediate checkpoints may need to be provided to ensure that the robot arm can effectively
    reach that desired end pose.

    - This feature would require a set (or sets) of intermediate checkpoints that represent the
      sequence of poses that the robot arm must follow. The automation program would loop through
      this list, reaching each of these intermediate poses, before reaching the final pose.
    - It must be noted that the method of reaching this intermediate poses may be abstracted
      further, as to provide a command name along with the corresponding data ('move_joints', [0,
      100, 0, 0, 0, 0]). This is simply to retain all data within the configuration.yaml file,
      though hard-coded sub-routines can be developed for such cases.
-   The generation of these routines is highly dependent on the configuration data and routines
    provided, given that the low-level robot arm commands, or the inverse kinematics, are
    directly handled by the mecademicpy API. Building an interface to more easily interact and
    program routines taking these into account will drastically improve the quality of the final
    routines.

