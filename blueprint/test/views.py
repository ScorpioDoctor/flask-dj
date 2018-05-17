from . import blueprint_app
from .models import db
from flask import render_template

@blueprint_app.route("/", methods=["GET", "POST"])
def index():
    return render_template("blueprint/test/index.html")

def test():
    return "hello, world"
