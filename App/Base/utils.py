# 私人代码，不属于flask_dj

import requests,random,json

def _sendSms(phone, code):
    return True

def send_vcode(phone):
    vcode = _generate_vcode()
    status = _sendSms(phone, vcode)
    return status, vcode

def _generate_vcode():
    result = []
    data = [str(x) for x in range(9)]
    for _ in range(4):
        result.append(random.choice(data))
    return ''.join(result)
        
