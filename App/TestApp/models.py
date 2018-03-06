

from flask_login import UserMixin
from flask_dj.globals import db


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

    def get_id(self):
        return self.username
    

