# 所有蓝图下的py文件必须在__init__.py最后一行导入，不然不生效
from flask_dj.models import db, User # 用到全局model请在这导入，如果没用到，只需要导入db就行


class test_model2(db.Model):
    __tablename__ = "test_model2"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    children = db.relationship("test_model", lazy="dynamic")


class test_model(db.Model):
    __tablename__ = "test_model"

    id = db.Column(db.Integer, primary_key=True)
    test_model_username = db.Column(db.String(64))
    test_model_password = db.Column(db.String(64))

    a = db.Column(db.Integer, db.ForeignKey("test_model2.id"))

