from flask import Flask
from config import Config

app = Flask(__name__)
config = Config()

@app.route('/')
def hello_world():  # put application's code here
    return config.NAME


if __name__ == '__main__':
    app.run()
