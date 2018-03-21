
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_dj.globals import admin
from .model import db, User


# 您的代码

# 国际化汉化
class DB_USER(ModelView):
    column_labels = dict(username='用户名', password='密码')
    form_columns = ['username', 'password']

admin.add_view(DB_USER(User, db.session, name="用户管理"))

