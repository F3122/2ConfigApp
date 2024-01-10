from flask import Flask
from config import Config
from config_student import ConfigStudent

app = Flask(__name__)
config = Config()
configStudent = ConfigStudent()

@app.route('/')
def hello_world():  # put application's code here
    return f"{config.NAME}, {configStudent.MAJOR}"


if __name__ == '__main__':
    app.run()
