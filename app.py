from flask import Flask
from flask_dj.app import initFlask

app = Flask(__name__)
initFlask(app)
if __name__ == '__main__':
    app.run()

