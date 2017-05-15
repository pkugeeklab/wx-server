from urllib import request, parse
import json
from getAccessToken import getToken

def newNotification(filename, touser, key1, key2, key3, key4, first, remark):
    ACCESS_TOKEN = getToken()
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=ACCESS_TOKEN'
    url = url.replace('ACCESS_TOKEN', ACCESS_TOKEN)
    headers = {
        'Content-Type': 'application/json'
    }
    data = open(filename, 'rb').read(-1).decode()
    print(type(data))
    print(touser)
    data = data.format(touser, key1, key2, key3, key4, first, remark).encode()
    req = request.Request(url, data=data, headers=headers)
    res = request.urlopen(req)
    data = res.read().decode()
    return data
