
from flask import Flask, g
from importlib import import_module
from .globals import *
from .config import *
from App.Base.model import User
from .admin import IndexView            # 后台主页

class FlaskDJ(Flask):
    def __init__(self, *args, **kwargs):
        super(FlaskDJ, self).__init__(*args, **kwargs)

        # 初始化config.py
        self.config.from_object(__name__)

        # 初始化功能库
        db.init_app(app=self)
        login_manager.init_app(app=self)
        babel.init_app(app=self)
        bootstrap.init_app(app=self)
        admin.init_app(app=self, index_view=IndexView())
        moment.init_app(app=self)
        migrate.init_app(app=self, db=db)
        

        # 导入蓝图
        for module_name, module_url in INSTALL_APP.items():
            self.import_app(module_url, module_name)

        
        @self.before_first_request
        def _before_first_request():
            # 初始化数据表
            db.create_all()

            # 创建超级用户
            User.query.filter_by(username=SUPER_USER['USERNAME']).delete(synchronize_session=False)
            user = User(username=SUPER_USER['USERNAME'], password=SUPER_USER['PASSWORD'])
            db.session.add(user)
            db.session.commit()


    def import_app(self, app_url, app_name):
            (module_url, module_name) = app_url, app_name

            module_admin = import_module('%s.%s' % (module_name, 'admin'))
            module_views = import_module('%s.%s' % (module_name, 'views'))
            module_model = import_module('%s.%s' % (module_name, 'model'))
            module_urls = import_module('%s.%s' % (module_name, 'urls'))

            # 加载后台任务模块
            try:
                module_task = import_module('%s.%s' % (module_name, 'task'))
                for task_func_name in dir(module_task):
                    task_func = getattr(module_task, task_func_name)
                    if task_func and getattr(task_func, 'start', None):
                        task_func().start()
            except ImportError as e:
                if SHOW_ERROR:
                    print(e)
                    print('ImportError: {0}.task'.format(app_name))

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











