import os
import json

class ConfigStudent():
    def __init__(self):
        working_directory = os.getcwd()
        config_file = "configStudent.json"
        config_path = os.path.join(working_directory, config_file)
        with open(config_path, "r") as config_file_path:
            config = json.load(config_file_path)
            self.AGE = config["AGE"]
            self.MAJOR = config["MAJOR"]