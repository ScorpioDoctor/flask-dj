
# 这个是AdminIndexView  
# 就是首页，对应url：/admin/
# 所有admin的url都会经过首页
# 所以这个一般用来检验登录权限

from flask_admin import AdminIndexView, expose

class DJAdminIndexView(AdminIndexView):
    # 返回原始首页
    @expose('/')
    def index(self):
        return self.render('admin/index.html')