

from flask_login import UserMixin
from .globalvar import db, login_manager


# 关于admin权限，没做
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

    def get_id(self):
        return self.username

# flask-login  对应User.get_id函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

