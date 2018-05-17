
from myproject.framework._globals import get_globals_object
admin = get_globals_object("admin")

from .admin.views import DJTestView

# DJAdminIndexView的汉化在globalvar里面改
admin.add_view(DJTestView("这是babel测试"))

