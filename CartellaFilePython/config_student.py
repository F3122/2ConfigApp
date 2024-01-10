import os
import json

class config_student():
    def __init__(self):
        working_directory = os.getcwd()
        config_file = "config.json"
        config_path = os.path.join(working_directory, "config.json")
        with open(config_path, "r") as config_file_path:
            self.config = json.load(config_file_path)
            self.AGE = config_student["AGE"]
            self.MAJOR = config_student["MAJOR"]