import os
import json

class Config():
    def __init__(self):
        working_directory = os.getcwd()
        config_file = "config.json"
        config_path = os.path.join(working_directory, config_file)
        with open(config_path, "r") as config_file_path:
            config = json.load(config_file_path)
            self.ID = config["ID"]
            self.NAME = config["NAME"]
            self.LASTNAME = config["LASTNAME"]
            self.GENDER = config["GENDER"]
