
# 这个没导入
from flask_admin import BaseView, expose

class DJTestView(BaseView):
    # 返回原始首页
    @expose('/')
    def index(self):
        return self.render('admin/test.html')


