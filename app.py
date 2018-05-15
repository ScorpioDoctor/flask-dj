from flask import Flask
from flask_dj.app import initFlask
from flask_dj.globalvar import db

app = Flask(__name__)
initFlask(app)
if __name__ == '__main__':
    from flask_dj.babel.admin import regisiter
    """ 查看sql语句
    app.app_context().push()
    db.drop_all()
    db.create_all()
    """
    app.run()

