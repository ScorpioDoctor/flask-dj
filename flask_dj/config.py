

SERVER_NAME = '127.0.0.1:8888'


INSTALL_APP = {
    'App.TestApp': '', # 蓝图url
}


#Flask自带的app.config
SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
