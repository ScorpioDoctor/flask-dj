# flask-dj  [gpl-2.0]
# flask结构化导入蓝图

只需要在config.py 插入一行代码，就能轻松解决循环导入的问题

```python
# 插入蓝图
INSTALL_APP = {
    'App.Base': '', # 蓝图和url
}
```

把flask配置和代码分离

```python
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


#--------------------------------------------------
# 下面是Flask自带的app.config

# ip端口(禁止使用，否则flask-login失效)
# SERVER_NAME = '127.0.0.1:5000'

# 调试模式
DEBUG = True

# 安全key
SECRET_KEY = 'c20ad4d76fe97759aa27a0c99bff6712'

# 数据库
SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = False       # request返回后自动提交

# 模板自动重载(好像没鸟用)
# TEMPLATES_AUTO_RELOAD = True

```