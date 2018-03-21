
from flup.server.fcgi import WSGIServer
from flask_cli import FlaskCLI, FlaskGroup
from app import app

# @app.cli.command(with_appcontext=True)
# flask_cli 没啥鸟功能，还不支持输入参数, 默认已经切换到app上下文了
# 能用的只有app.cli.command， 对应的就是函数名
# 使用flask --help就看到当前定义的函数名了


@app.cli.command()
def runfcgi():
    DEBUG = app.config.get('DEBUG', None)
    if DEBUG:
        # fcgi模式用于发布,debug标志不能设置为True
        raise ValueError('The fcgi mode is used for publication, and the DEBUG flag can not be set to True')
    SERVER_NAME = app.config.get('SERVER_NAME', None)
    MULTIPROCESS = app.config.get('MULTIPROCESS', None)
    if SERVER_NAME is None:
        SERVER_NAME = 'localhost:5000'
    host, port = SERVER_NAME.split(':')
    WSGIServer(app, bindAddress=(host, port), multiprocess=MULTIPROCESS).run()


if __name__ == '__main__':
    FlaskCLI(app)
