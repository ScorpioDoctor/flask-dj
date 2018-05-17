

from . import blueprint_app
from .views import test

blueprint_app.add_url_rule("/test", view_func=test, methods=["GET", "POST"])