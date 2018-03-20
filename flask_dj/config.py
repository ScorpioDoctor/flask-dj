
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


# 下面是Flask自带的app.config

SECRET_KEY = 'c20ad4d76fe97759aa27a0c99bff6710'

SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 模板自动重载(好像没鸟用，必须app.jinja_env.auto_reload = True)
TEMPLATES_AUTO_RELOAD = True
