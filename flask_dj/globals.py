
from flask_login import LoginManager
from flask_babelex import Babel
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from .admin import IndexView

# 这里只能写flask扩展插件
db = SQLAlchemy()
login_manager = LoginManager()
babel = Babel(default_locale="zh_cn")
admin = Admin(name='后台内容管理', index_view=IndexView(), template_mode="bootstrap3")







