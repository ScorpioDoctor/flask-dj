
from flask import Flask
from importlib import import_module
from .globals import *
from .config import *
from App.Base.models import User

class FlaskDJ(Flask):
    def __init__(self, *args, **kwargs):
        super(FlaskDJ, self).__init__(*args, **kwargs)

        # 初始化config.py
        self.config.from_object(__name__)

        # 初始化功能库
        db.init_app(self)
        login_manager.init_app(self)
        babel.init_app(self)
        admin.init_app(self)

        # 导入蓝图
        for module_name, module_url in INSTALL_APP.items():
            self.import_app(module_url, module_name)

        # 初始化数据表
        self.app_context().push()
        db.create_all(app=self)
        
        # 创建超级用户
        User.query.filter_by(username=SUPER_USER['USERNAME']).delete(synchronize_session=False)
        db.session.commit()
        user = User(username=SUPER_USER['USERNAME'], password=SUPER_USER['PASSWORD'])
        db.session.add(user)
        db.session.commit()



    def import_app(self, app_url, app_name):
            (module_url, module_name) = app_url, app_name

            module_admin = import_module('%s.%s' % (module_name, 'admin'))
            module_views = import_module('%s.%s' % (module_name, 'views'))
            module_models = import_module('%s.%s' % (module_name, 'models'))
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











