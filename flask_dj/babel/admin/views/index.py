
# 这个是AdminIndexView  
# 就是首页，对应url：/admin/
# 所有admin的url都会经过首页
# 所以这个一般用来检验登录权限

from flask_admin import AdminIndexView, expose

class DJAdminIndexView(AdminIndexView):
    def is_accessible(self):
        """
        校验权限是否可登陆
        """
        return True
    def inaccessible_callback(self, name, **kwargs):
        """
        权限校验失败,执行哪些跳转
        """
        return abort(403)

    # 返回原始首页
    @expose('/')
    def index(self):
        return self.render('admin/index.html')