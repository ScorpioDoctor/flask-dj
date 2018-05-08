#--------------------------------------------------
# 下面是Flask自带的app.config

# ip端口(注册localhost和127.0.0.1是不通用的)
SERVER_NAME = 'localhost:5000'

# 下面两个不属于flask变量，自定义的在manage.py里面
fcgi_multiprocess = True
fcgi_multithread = True

# 调试模式
DEBUG = True

# 安全key  flask-login用到
SECRET_KEY = 'c20ad4d76fe97759aa27a0c99bff6712'

# 数据库
SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Jinja2模板自动重载(好像没鸟用),已经写在globals里面了
# TEMPLATES_AUTO_RELOAD = True

