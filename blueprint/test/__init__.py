
import os
from flask import Blueprint

# 懒得写，直接用目录名代替，反正目录名称不会重复
blueprint_name = os.path.dirname(__file__)
blueprint_name = os.path.basename(blueprint_name)

blue_app = Blueprint(blueprint_name, __name__)


# 导入生效
from . import models, views

