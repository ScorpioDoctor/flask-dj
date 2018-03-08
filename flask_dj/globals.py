
from flask_login import LoginManager
from flask_babelex import Babel
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login_manager = LoginManager()
babel = Babel()
admin = Admin()






