# 框架不要改，请改app.py
import os

from importlib import import_module
from . import _globals

class FlaskAlpha:
    def __init__(self, flask_app, config_module, blueprint_dirname="blueprint"):
        self.flask_app = flask_app
        setattr(_globals, "app", self)
        self.init_config(config_module)
        self.init_app_before()
        self.init_app()
        self.init_middleware()
        self.init_blueprint(blueprint_dirname)
        self.init_done()

    def run(self, *args, **kwargs):
        self.flask_app.run(*args, **kwargs)

    def init_config(self, config_module):
        self.flask_app.config.from_object(config_module)
        self.flask_app.jinja_env.auto_reload = getattr(config_module, 'DEBUG', False)
    
    def init_app_before(self):
        pass

    def init_app(self):
        pass

    def init_done(self):
        pass

    def init_middleware(self):
        """
        例如:
            @app.before_first_request
            def _before_first_request():
                pass
        """
        pass

    def init_blueprint(self, blueprint_dirname):
        dirs = os.listdir(blueprint_dirname)
        for _dir in dirs:
            _module = import_module("{}.{}".format(blueprint_dirname, _dir))
            _urls = getattr(_module, "blueprint_app_url", None)
            for _url in _urls:
                self.flask_app.register_blueprint(_module.blueprint_app, url_prefix=_url)

    def regisiter_flask_ext(self, ext_name, ext_module):
        if getattr(_globals, ext_name, None) == None and \
            getattr(self, ext_name, None) == None:
            ext_module.init_app(self.flask_app)
            setattr(_globals, ext_name, ext_module)
            setattr(self, ext_name, ext_module)
        else:
            raise AttributeError('Flask扩展注册错误: "{}"已经存在'.format(ext_name))

    def regisiter_globlas_object(self, name, value):
        if getattr(_globals, name, None) == None:
            setattr(_globals, name, value)
        else:
            raise AttributeError('属性注册错误: "{}"已经存在'.format(name))
    
