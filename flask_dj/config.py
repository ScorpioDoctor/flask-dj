#------------------flask_dj内部变量--------------------------------
# 插入蓝图
INSTALL_APP = {
    'App.Base': '', # 蓝图和url
}

# 创建超级用户
SUPER_USER = {
    'USERNAME': 'admin',
    'PASSWORD': 'admin'
}

# 导入thread错误信息
SHOW_ERROR = False


# globals.py
# 国际化
BABEL_DEFAULT_LOCALE = 'zh_cn'

# admin
ADMIN_NAME = 'hello'
TEMPLATE_MODE = "bootstrap3"


# manage.py
# flup多进程，这里我用的是fcgi
MULTIPROCESS = True

#--------------------------------------------------
# 下面是Flask自带的app.config

# ip端口(调试模式下, flask-login有可能会导致admin无法登录，如果出问题，请把这个禁止，用app.run(host=ip, host=端口))
SERVER_NAME = 'localhost:5000'

# 调试模式
DEBUG = False

# 安全key
SECRET_KEY = 'c20ad4d76fe97759aa27a0c99bff6712'

# 数据库
SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 模板自动重载(好像没鸟用)
# TEMPLATES_AUTO_RELOAD = True

