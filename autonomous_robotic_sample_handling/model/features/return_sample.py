class ReturnSample:
    def __init__(self, model, *args):
        self.model = model
        self.configuration = self.model.configuration["routine_config"]
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
        print(self.get_loading_zone())
        

    def get_loading_zone(self):
        # Check which loading zone calculation method is used
        flag = self.configuration['environment']['loading_zone']['flag']
        if flag is True:
            x = self.configuration["environment"]["loading_zone"]["pose"]["x"]
            y = self.configuration["environment"]["loading_zone"]["pose"]["y"]
            z = self.configuration["environment"]["loading_zone"]["pose"]["z"]
            Rx = self.configuration["environment"]["loading_zone"]["pose"]["Rx"]
            Ry = self.configuration["environment"]["loading_zone"]["pose"]["Ry"]
            Rz = self.configuration["environment"]["loading_zone"]["pose"]["Rz"]
        else:
            x = self.configuration["environment"]["microscope"]["x"]
            y = self.configuration["environment"]["microscope"]["y"]
            z = self.configuration["environment"]["microscope"]["z"]
            Rx = self.configuration["environment"]["microscope"]["Rx"]
            Ry = self.configuration["environment"]["microscope"]["Ry"]
            Rz = self.configuration["environment"]["microscope"]["Rz"]

        return [x, y, z, Rx, Ry, Rz]

    def pre_func_signal(self):
        """Prepare device thread to run this feature"""
        self.sample_height = 10
        self.engage_header_distance = 10
        self.loading_zone = self.get_loading_zone()
        pass

    def in_func_signal(self):
        """set devices before snaping an image"""
        # Position robot arm in front of loading zone
        x, y, z, Rx, Ry, Rz = self.loading_zone
        self.robot_arm.move_lin(x, y, z + self.sample_height, Rx, Ry, Rz)
        self.robot_arm.delay(1)

        # Place sample within vial
        self.robot_arm.move_lin_rel_trf(self.sample_height, 0, 0, 0, 0, 0)
        self.robot_arm.open_gripper()
        self.robot_arm.delay(1)

        # Disengage robot arm from loading zone
        self.robot_arm.move_lin_rel_trf(0, 0, -self.engage_header_distance, 0, 0, 0)
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
