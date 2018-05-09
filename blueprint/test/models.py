# 所有蓝图下的py文件必须在__init__.py最后一行导入，不然不生效
from flask_dj.models import db, User # 用到全局model请在这导入，如果没用到，只需要导入db就行

