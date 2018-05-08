from flask import Blueprint
from flask_dj.models import db, User

blue_app = Blueprint("test", __name__)

@blue_app.route("/")
def index():
    return "hello, world"

@blue_app.route("/add/<info>")
def index2(info):
    return "hello, world"