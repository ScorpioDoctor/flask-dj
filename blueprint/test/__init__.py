
import os
from flask import Blueprint

blueprint_name = os.path.dirname(__file__)
blueprint_name = os.path.basename(blueprint_name)
blueprint_app = Blueprint(blueprint_name, __name__)
blueprint_app_url = ""  # 蓝图的url
# 固定导入顺序
from . import models, admin, views, urls

