from flask import  Blueprint


app = Blueprint('TestApp', __name__)





def index():
    return 'this is index', 200

@app.route('/test')
def my_test():
    return 'this is my_test', 200