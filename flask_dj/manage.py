
from flup.server.fcgi import WSGIServer
from flask_cli import FlaskCLI, FlaskGroup
from .globalvar import app

# @app.cli.command(with_appcontext=True)
# flask_cli 没啥鸟功能，还不支持输入参数, 默认已经切换到app上下文了
# 能用的只有app.cli.command， 对应的就是函数名
# 使用flask --help就看到当前定义的函数名了


@app.cli.command()
def runfcgi():
    DEBUG = app.config.get('DEBUG', None)
    if DEBUG:
        # fcgi模式用于发布,debug标志不能设置为True
        raise ValueError('FCGI不支持调试模式')
    
    server = SERVER_NAME.split(":")
    server_ip, server_port = server[0], int(server[1])
    WSGIServer(app, bindAddress=(server_ip, server_port), multiprocess=app.config.get('fcgi_multiprocess', False), multithread=app.config.get('fcgi_multithread', False)).run()


if __name__ == '__main__':
    FlaskCLI(app)
