# 所有蓝图下的py文件必须在__init__.py最后一行导入，不然不生效
from . import blue_app
from .models import db, User
from flask import render_template

@blue_app.route("/")
def index():
    return render_template("blueprint/test/index.html")

@blue_app.route("/add/<info>")
def index2(info):
    
    return "hello, world"