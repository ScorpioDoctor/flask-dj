from flask_admin import Admin
from .framework.alpha import FlaskAlpha
from i8n.admin.views import DJAdminIndexView

from flask_login import LoginManager
from flask_babelex import Babel
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment



# 未初始化，错误方法，正确方法请查看: init_app
# from .models import User

class MyFlaskApp(FlaskAlpha):
    def init_app_before(self):
        # 全部注册到self和framework._globlas
        self.regisiter_flask_ext("db", SQLAlchemy())
        self.regisiter_flask_ext("login_manager", LoginManager())
        self.regisiter_flask_ext("babel", Babel())
        self.regisiter_flask_ext("admin", Admin(name=self.flask_app.config["ADMIN_NAME"], index_view=DJAdminIndexView(name="首页")))
        self.regisiter_flask_ext("bootstrap", Bootstrap())
        self.regisiter_flask_ext("migrate", Migrate(db=self.db))
        self.regisiter_flask_ext("moment", Moment())

    def init_app(self):

        from .models import User
        from i8n import regisiter

        self.regisiter_globlas_object("User", User)
        pass

    def init_done(self):
        pass
