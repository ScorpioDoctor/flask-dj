from flask_dj import FlaskDJ
from flask_dj.config import DEBUG

app = FlaskDJ(__name__)

if __name__ == '__main__':
    if DEBUG:
        app.jinja_env.auto_reload = True
    app.run(host="localhost", port=5000)

