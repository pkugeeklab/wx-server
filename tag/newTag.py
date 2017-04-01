from urllib import request, parse
import json
from getAccessToken import getToken

def newTag(tagName):
    ACCESS_TOKEN = getToken()
    url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=ACCESS_TOKEN'
    url = url.replace('ACCESS_TOKEN', ACCESS_TOKEN)
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'tag': {
            'name': tagName
        }
    }, ensure_ascii=False).encode()
    req = request.Request(url, data=data, headers=headers)
    res = request.urlopen(req)
    data = res.read().decode()
    return data
