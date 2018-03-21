import click
from flup.server.fcgi import WSGIServer

    # fcgi部署项目
    #WSGIServer(app, bindAddress=("127.0.0.1", 9000), multiprocess=True).run()