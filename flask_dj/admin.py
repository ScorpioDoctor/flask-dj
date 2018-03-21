from flask_admin.base import AdminIndexView, expose
from flask_login import current_user
from flask import redirect

# Admin的Index主页，一般用于admin权限校验

class IndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_anonymous or current_user.is_authenticated == False:
            return False
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login')

    @expose('/')
    def index(self):
        return self.render('AdminIndex/index.html')