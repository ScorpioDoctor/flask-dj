
# 这个是AdminIndexView  
# 就是首页，对应url：/admin/
# 所有admin的url都会经过首页
# 所以这个一般用来检验登录权限

from flask_admin import AdminIndexView, expose

class DJAdminIndexView(AdminIndexView):
    def is_accessible(self):
        """
            Override this method to add permission checks.

            Flask-Admin does not make any assumptions about the authentication system used in your application, so it is
            up to you to implement it.

            By default, it will allow access for everyone.
        """
        return True
    def inaccessible_callback(self, name, **kwargs):
        """
            Handle the response to inaccessible views.

            By default, it throw HTTP 403 error. Override this method to
            customize the behaviour.
        """
        return abort(403)
        
    # 返回原始首页
    @expose('/')
    def index(self):
        return self.render('admin/index.html')