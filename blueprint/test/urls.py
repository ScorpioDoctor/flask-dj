

from . import blue_app
from .views import test

# 统一化管理urls
blue_app.add_url_rule("/test", view_func=test, methods=["GET", "POST"])