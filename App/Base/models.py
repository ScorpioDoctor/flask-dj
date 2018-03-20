

from flask_login import UserMixin
from flask_dj.globals import db, login_manager

# 关于admin权限，没做
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

    def get_id(self):
        return self.username
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

# 您的代码
class SendSMS(db.Model):
    __tablename__ = 'SendSMS'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(15))
    vcode = db.Column(db.String(6), default='')
    count = db.Column(db.Integer, default=0)

class ApplyInfo(db.Model):
    __tablename__ = 'ApplyInfo'
    id = db.Column(db.Integer, primary_key=True)
    je = db.Column(db.String(10))               # 金额
    yt = db.Column(db.String(10))               # 用途
    phone = db.Column(db.String(15))            # 手机
    name = db.Column(db.String(10))             # 名字
    city = db.Column(db.String(10))             # 城市