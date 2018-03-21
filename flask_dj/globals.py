
from flask_login import LoginManager    # 用户登录
from flask_babelex import Babel         # 国际化文字翻译
from flask_admin import Admin           # 后台管理
from flask_sqlalchemy import SQLAlchemy # 数据库
from flask_bootstrap import Bootstrap   # 前端框架
from flask_migrate import Migrate       # 数据库迁移
from flask_moment import Moment         # 全球化统一时间

from .config import *

# 这里只能写flask扩展插件
db = SQLAlchemy()
login_manager = LoginManager()
babel = Babel(default_locale=BABEL_DEFAULT_LOCALE)
admin = Admin(name=ADMIN_NAME, template_mode=TEMPLATE_MODE)
bootstrap = Bootstrap()
migrate = Migrate()
moment = Moment()






