
from flask_dj.globals import admin
from flask_admin.contrib.sqla import ModelView


from .models import db, User
admin.add_view(ModelView(User, db.session, name="用户"))
