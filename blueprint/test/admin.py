
from flask_admin.contrib.sqla import ModelView
from .models import db, LoginUser, ProxyManager

from myproject.framework._globals import get_globals_object
admin = get_globals_object("admin")

admin.add_view(ModelView(ProxyManager, session=db.session, name="代理"))
admin.add_view(ModelView(LoginUser, session=db.session, name="用户信息"))
