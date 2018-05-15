# 所有蓝图下的py文件必须在__init__.py最后一行导入，不然不生效
from flask_dj.models import db, User # 用到全局model请在这导入，如果没用到，只需要导入db就行


class LoginUser(db.Model):
    __tablename__ = "LoginUser"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    proxyManager = db.Column(db.Integer, db.ForeignKey("ProxyManager.id"))


class ProxyManager(db.Model):
    __tablename__ = "ProxyManager"
    id = db.Column(db.Integer, primary_key=True)
    proxyName = db.Column(db.String(64))
    allUser = db.relationship("LoginUser", lazy="dynamic")


