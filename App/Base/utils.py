# 私人代码，不属于flask_dj

import requests,random,json


def send_vcode(phone):
    return True, '1234'

def _generate_vcode():
    result = []
    data = [str(x) for x in range(9)]
    for _ in range(4):
        result.append(random.choice(data))
    return ''.join(result)
        
