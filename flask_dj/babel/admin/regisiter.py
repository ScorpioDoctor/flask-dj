
from flask_dj.globalvar import admin
from .views import DJTestView

# DJAdminIndexView的汉化在globalvar里面改
admin.add_view(DJTestView("这是babel测试"))

