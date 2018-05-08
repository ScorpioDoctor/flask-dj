

from flask_dj.config import *
import flask_dj.config as config
from flask_dj.globalvar import *
import flask_dj.globalvar as globalvar


from blueprint.test import blue_app



def initFlask(app):
    # ------下面部分，禁止修改--------
    globalvar.app = app
    # 初始化配置
    app.config.from_object(config)
    # 设置Jinja2自动重载模板
    app.jinja_env.auto_reload = getattr(config, 'DEBUG', False)


    # ------下面部分，随便修改--------
    # 这里初始化你的插件，一般是globlas定义的
    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app)
    admin.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)

    # 这里注册你的中间件
    """
    @app.before_first_request
    def _before_first_request():
        pass
    """
    # 这里注册你的蓝图
    app.register_blueprint(blue_app, url_prefix="")
    # app.register_blueprint(blue_app, url_prefix="/home")

    # 这里注册其他插件