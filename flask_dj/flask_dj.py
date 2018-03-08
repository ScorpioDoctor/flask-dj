
from flask import Flask
from .globals import *
from .config import *
from importlib import import_module
from threading import Thread




class FlaskDJ(Flask):
    def __init__(self, *args, **kwargs):
        super(FlaskDJ, self).__init__(*args, **kwargs)

        # 初始化config.py
        self.config.from_object(__name__)

        # 初始化功能库
        login_manager.init_app(self)
        db.init_app(self)
        babel.init_app(self)
        admin.init_app(self)
        """
        # 导入app
        for module_name, module_url in INSTALL_APP.items():
            module_admin = import_module('%s.%s' % (module_name, 'admin'))
            module_views = import_module('%s.%s' % (module_name, 'views'))
            module_models = import_module('%s.%s' % (module_name, 'models'))
            module_urls = import_module('%s.%s' % (module_name, 'urls'))
            module_thread = import_module('%s.%s' % (module_name, 'thread'))

            for thread_func_name in dir(module_thread):
                thread_func = getattr(module_thread, thread_func_name)
                if isinstance(thread_func, Thread):
                    thread_func.start()


            # 蓝图url
            for rule in module_urls.urls:
                if len(rule) == 3:
                    (rule, view, methods) = rule
                else:
                    (rule, view) = rule
                    methods = None
                module_views.app.add_url_rule(rule, view_func=view, methods=methods)
            # 注册蓝图
            self.register_blueprint(module_views.app, url_prefix=module_url)
        """
        for module_name, module_url in INSTALL_APP.items():
            self.import_app(module_url, module_name)

        # 初始化数据表
        self.app_context().push()
        db.create_all(app=self)


    def import_app(self, app_url, app_name):
        try:
            # 动态导入app

            (module_url, module_name) = app_url, app_name

            import_name = 'admin'
             
            module_admin = import_module('%s.%s' % (module_name, import_name))
            import_name = 'views'
            module_views = import_module('%s.%s' % (module_name, import_name))
            import_name = 'models'
            module_models = import_module('%s.%s' % (module_name, import_name))
            import_name = 'urls'
            module_urls = import_module('%s.%s' % (module_name, import_name))
            import_name = 'thread'
            module_thread = import_module('%s.%s' % (module_name, import_name))

            for thread_func_name in dir(module_thread):
                thread_func = getattr(module_thread, thread_func_name)

                if thread_func and getattr(thread_func, 'start', None):
                    thread_func().start()

            # 蓝图url
            for rule in module_urls.urls:
                if len(rule) == 3:
                    (rule, view, methods) = rule
                else:
                    (rule, view) = rule
                    methods = None
                module_views.app.add_url_rule(rule, view_func=view, methods=methods)
            # 注册蓝图
            self.register_blueprint(module_views.app, url_prefix=module_url)
        except Exception as e:
            print(e)
            print('Import app error, app_name:"%s.%s" app_url:"%s"' % (app_name, import_name, app_url))
            pass










