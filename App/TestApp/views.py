from flask import  Blueprint
from .thread import queue_login, queue_basicInfo, queue_moreInfo

app = Blueprint('TestApp', __name__)




# route /
def index():
    queue_login.put('123')
    return 'this is index', 200

@app.route('/test')
def my_test():
    return 'this is my_test', 200