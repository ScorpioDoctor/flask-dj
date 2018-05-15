from flask_dj.globalvar import admin
from flask_admin.contrib.sqla import ModelView

from .models import db, test_model2, test_model


admin.add_view(ModelView(test_model, session=db.session, name="基础模型1"))
admin.add_view(ModelView(test_model2, session=db.session, name="基础模型2"))
