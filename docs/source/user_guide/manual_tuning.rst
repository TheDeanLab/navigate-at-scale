======================================
Manual Tuning
======================================

In this guide, we will discuss in detail how to manually tune the system for automatically
generating the appropriate control routines. The desired loading zone will be selected and
adjusted using the motor and the Kinesis software. The robot arm will then be adjusted using the
Mecaportal software to identify the loading zone and microscope staging area locations relative
to the robot arm base. Any additional configuration parameters can then be reviewed and adjsuted
before commencing the operation.

.. image:: user_guide/images/system_view_back.png
  :alt: System View of Routine (Back)

Note that this can be somewhat of an iterative process, to identify a pose for the robot arm and
adjust the loading zone with the motor accordingly.

----------------

Loading Zone Setup
-------------------------------------

To start, a clear loading zone must be defined before the robot arm can be used to locate said
loading zone.

#. Connect to the motor for the carousel using the Kinesis software. This will be used to rotate
   the carousel in position to set up the loading zone appropriately.

#. Select a vial slot to be the starting loading zone, typically that which
   corresponds to the first sample. This slot will be oriented to be closest to the robot arm.

#. Rotate the carousel such that the loading zone (first vial slot, etc.) is positioned closest
   to the robot arm, with the edge of the vial parallel to the base of the robot arm.

.. note::
    The loading zone and microscope staging area are intentionally aligned with the robot arm
    reference frame axes. This is to simplify the calculation and positioning of orientation,
    both during the tuning process and with MoveLin() operations.

4. Position the robot arm at the selected loading zone. Determine exactly the end-effector pose
   of the robot arm at the loading zone, which will be used in the configuration data file.

   a. Position the robot arm closely to the loading zone, avoiding any form of collision and
      with the correct orientation. This can be done either through manual control or through an
      initial tuning script.
   b. Manually jog the robot arm slowly to the exact loading zone. Position the gripper
      fingertips exactly around the header plate, keeping the header plate in the midpoint of the
      gripper fingertips. We seek to ensure a steady and balanced grip. The more precise the
      tuning, the better the performance.
   c. It is also important to note how far the gripper fingertips extend past the back of the
      vial. This positioning must be repeated for the microscope staging area to ensure
      appropriate placement of the header plate and sample back within the vial.

    .. image:: user_guide/images/gripper_fingertips_placement.jpg
         :alt: Gripper Fingertips Placement

.. warning::
    When manually tuning, ensure that the operator is simply *jogging* the robot, defined by
    right-clicking the decrease/increase buttons for a given variable in Cartesian/Joint Jog.
    This ensures that each click corresponds to a small increment of no more than 1 mm, or a
    similarly set step size. This greatly reduces the risk of causing any collateral damage or
    collisions with the environment while tuning the system. A normal click,, or a left-click,
    moves the robot at a faster pace, particularly so when no velocity limits are active. It is
    highly recommended to use a mouse for this process, as to ensure a proper right-click (and no
    accidental left clicks).

5. Repeat and re-iterate until the robot arm and the gripper fingertips are well adjusted for the
   loading zone, and vice-versa. Remove and re-insert both the vial and the header plate to view
   the positioning from multiple angles and ensure accuracy.

--------------

Tuning with Mecaportal
-----------------------------

The loading zone and microscope staging are locations can be found by operating the robot arm
with Mecaportal, keeping track of the end-effector pose. The process of utilizing this system is
briefly discussed in the previous section.

    .. image:: user_guide/images/mecaportal_end_effector_pose.jpg
         :alt: End-Effector Pose (Mecaportal)

The six Cartesian values represent the pose of the robot arm's end-effector with respect to its
reference frame, and it is this that needs to be added to the configuration data file. Manual
tuning with the robot arm and Mecaportal can be done to find the critical locations alongside
some guiding scripts. More on specific tuning considerations listed below:

.. note::
    It is recommended to set up some simple scripts for the robot arm (offline programs) to
    assist with the tuning procedure. Zero the joints on the robot arm and then apply a MoveLin()
    command to position the robot arm closer to the tuning zone of the target. It is critical
    that the orientation is clearly defined and that the end-effector pose is not in collision
    with any element of the environment. The robot arm can be simply jogged and manually moved
    from this point on.

- **Loading zone**:
    The methods of tuning the loading zone has already been discussed above, as an iterative
    process of selecting and tuning the loading zone itself. Note that the orienation of the
    robot is approximately ``(0, 90, 0)`` if the carousel is in front of the robot arm.

- **Microscope Staging Area**:
    The process of tuning for the microscope staging area is very similar to that of the loading
    zone. It is recommended to attach a sample to the staging area to help guide the positioning
    of the gripper fingertips. Note that the orientation of the robot arm may be ``(90, 0, -90)``
    or ``(-90, 0, 90)``, based on whether the microscope is positioned to the left or right of
    the robot arm.

    A couple of points of interest for gripper positioning with the microscope staging area:
        Ensure that the positioning of the gripper fingertips matches that of the loading zone
        tuning. They should extend past the header plate by about the same amount so that the
        robot arm is gripping the header plate at about the same location, so that when it
        attempts to place the sample back at the loading zone, the header plate and sample are
        returned without damaging the sample.

        Position the fingertips to be slightly shifted away from the shear direction. When the
        robot arm performs the shearing maneuver, there is a possibility for the grip to slightly
        shift out of place, or the orientation. The inclusion of a thin silicon layer greatly
        mitigates this risk, as would a slight time delay for the close_gripper() operation, but
        this shift of the microscope staging area tuning yielded the best results. Note that the
        magnets are strong enough such that this does not affect the alignment of the sample.

--------------

Additional Configuration Parameters
---------------------
At this point, the critical locations and data for the automation sequences have been collected
and any additional parameters or tuning variables can be determined before starting the program.
This typically refers to the *sample_height*, the *shear_distance*, or orientation adjustments
for the microscope staging area commands.
