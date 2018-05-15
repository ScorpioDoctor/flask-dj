from flask_dj.globalvar import admin
from flask_admin.contrib.sqla import ModelView

from .models import db, LoginUser, ProxyManager


admin.add_view(ModelView(ProxyManager, session=db.session, name="代理"))
admin.add_view(ModelView(LoginUser, session=db.session, name="用户信息"))
