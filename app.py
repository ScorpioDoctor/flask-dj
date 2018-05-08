from flask import Flask
from flask_dj.app import initFlask
if __name__ == '__main__':
    app = Flask(__name__)
    initFlask(app)
    app.run()

