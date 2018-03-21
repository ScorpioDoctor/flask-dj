# 私人代码，不属于flask_dj

import requests,random,json

def _sendSms(phone, code):
    content = {
        "name":"易优贷",
        "code":code,
        "minute":"5"}
    query = 'content=%s&mobile=%s&tNum=T150606060606' % (json.dumps(content),phone)
    # query = urllib.parse.quote(query)
    url = 'http://ali-sms.showapi.com/sendSms?%s' % query
    appcode = '37387f0a1c3045728d3666df9cca8569'
    headers = {
        'Authorization':'APPCODE %s' % appcode
    }
    r = requests.get(url, headers=headers)
    return(r.json()['showapi_res_body']['remark'].find('提交成功')>-1)


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
        
