from flask_dj import FlaskDJ

from flup.server.fcgi_fork import WSGIServer

app = FlaskDJ(__name__)
app.jinja_env.auto_reload = True


# fcgi部署项目
#WSGIServer(app, bindAddress="127.0.0.1:9000").run()

# 调试项目
app.run(host="127.0.0.1", port=5000, debug=False)

