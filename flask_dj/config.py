#--------------------------------------------------
# 下面是Flask自带的app.config

# ip端口(注册localhost和127.0.0.1是不通用的)
SERVER_NAME = 'localhost:5000' # 如果是fcgi设置错误，默认为0.0.0.0: 80


# 下面两个不属于flask变量，自定义的在manage.py里面
# 这是flup用的，只能选择其中一个
fcgi_multiprocess = True
fcgi_multithreaded = True
fcgi_multiplexed = True # 这个我也不知道干嘛用


# 调试模式
DEBUG = True

# 安全key  flask-login用到
SECRET_KEY = 'c20ad4d76fe97759aa27a0c99bff6712'

# 数据库
SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
# Jinja2模板自动重载(好像没鸟用),已经写在globals里面了
# TEMPLATES_AUTO_RELOAD = True

# babel 国际化
BABEL_DEFAULT_LOCALE = "zh_cn"
BABEL_DEFAULT_TIMEZONE = "Asia/Shanghai"

# admin
ADMIN_NAME = "后台管理"

