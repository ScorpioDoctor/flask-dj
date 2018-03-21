
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_dj.globals import admin
from .models import db, User


# 您的代码
admin.add_view(ModelView(User, db.session, name="用户"))

