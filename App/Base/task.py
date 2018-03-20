import time
from flask_dj.globals import admin
from threading import Thread
from .models import db, SendSMS



class ClearVcodeTask(Thread):
    def run(self, *args, **kwargs):
        while True:
            time.sleep(1)
            localtime = time.localtime()
            # 0点恢复验证码次数
            if localtime.tm_hour == 0 and localtime.tm_min == 0 :
                if admin.app:
                    admin.app.app_context().push()
                    SendSMS.query.delete()
                time.sleep(70)