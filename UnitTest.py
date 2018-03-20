
import unittest, tempfile, os
import json
from flask_dj import FlaskDJ

# 单元测试

def dispay_func_name(func):
    def inner(*args, **kwargs):
        print('FuncName: %s' % func.__name__)
        return func(*args, **kwargs)
    return inner

class MyTest(unittest.TestCase):
    def setUp(self):
        self.app = FlaskDJ(__name__)
        self.db_fd, self.app.config['DATABASE'] = tempfile.mkstemp()
        self.client = self.app.test_client()
    
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.app.config['DATABASE'])

    @dispay_func_name
    def test_1_sendsms(self):
        print(self.client.post(base_url + '/sendsms',data={
                'phone': '1334567890',
        }).data.decode())

    @dispay_func_name
    def test_2_apply(self):
        print(self.client.post(base_url + '/apply',data={
                'je': '100万',
                'yt': 'yl',
                'phone': '1334567890',
                'name': '老王',
                'city': '贵港市',
                'vcode': '1234',
        }).data.decode())
        

unittest.main()
