
from flask_login import LoginManager    # 用户登录
from flask_babelex import Babel         # 国际化文字翻译
from flask_admin import Admin           # 后台管理
from flask_sqlalchemy import SQLAlchemy # 数据库
from flask_bootstrap import Bootstrap   # 前端框架
from flask_migrate import Migrate       # 数据库迁移
from flask_moment import Moment         # 全球化统一时间
app = None # 这个不能改


from .config import * # 下面注册插件可能用到某些config的变量

# 这里注册你的扩展插件
db = SQLAlchemy()
login_manager = LoginManager()
babel = Babel()
admin = Admin()
bootstrap = Bootstrap()
migrate = Migrate()
moment = Moment()