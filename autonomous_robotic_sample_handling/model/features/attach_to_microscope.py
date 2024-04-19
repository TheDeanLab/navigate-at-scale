class AttachToMicroscope:
    def __init__(self, model, *args):
        self.model = model
        self.robot_arm = self.model.active_microscope.plugin_devices["robot_arm"]

        self.config_table = {
            "signal": {
                "init": self.pre_func_signal,
                "main": self.in_func_signal,
                "end": self.end_func_signal,
                "cleanup": self.cleanup_func_signal,
            },
            "data": {
                "init": self.pre_func_data,
                "main": self.in_func_data,
                "end": self.end_func_data,
                "cleanup": self.cleanup_func_data,
            },
            "node": {
                "node_type": "multi-step",  # "multi-step" or "one-step"
                "device_related": True,  # True or False
                "need_response": True,  # True or False
            },
        }

    def pre_func_signal(self):
        """Prepare device thread to run this feature"""
        self.microscope = [10, 10, 10, 0, 90, 0]
        self.microscope_tolerance = 10
        self.engage_header_distance = 10
        pass

    def in_func_signal(self):
        """set devices before snaping an image"""
        x, y, z, Rx, Ry, Rz = self.microscope

        # Position robot arm in front of the microscope
        self.robot_arm.move_lin(x, y - self.engage_header_distance, z - self.microscope_tolerance, Rx, Ry, Rz)

        # Engage microscope
        self.robot_arm.move_lin_rel_trf(0, 0, self.engage_header_distance, 0, 0, 0)
        self.robot_arm.move_lin_rel_trf(-self.microscope_tolerance, 0, 0, 0, 0, 0)
        self.robot_arm.open_gripper()

        # Disengage microscope
        self.robot_arm.move_lin_rel_trf(0, 0, -self.engage_header_distance * 2, 0, 0, 0)

        pass

    def end_func_signal(self):
        """decide if this feature ends after snaping an image"""
        pass

    def pre_func_data(self):
        """Prepare data thread to run this feature"""
        pass

    def in_func_data(self, frame_ids):
        """Deal with images"""
        pass

    def end_func_data(self):
        """Decide if this feature ends"""
        pass

    def cleanup_func_signal(self):
        """Cleanup"""
        pass

    def cleanup_func_data(self):
        """Cleanup"""
        pass
