# 所有蓝图下的py文件必须在__init__.py最后一行导入，不然不生效
from . import blue_app
from .models import db, User
from flask import render_template



# 方法一: 装饰器
@blue_app.route("/", methods=["GET", "POST"])
def index():
    return render_template("blueprint/test/index.html")

# 方法二: 可以实现类似django的urls.py 
def test():
    return "hello, world"
