from urllib import request, parse
import json
from getAccessToken import getToken

def addToTag(openid, tagid):
    ACCESS_TOKEN = getToken()
    print(openid, tagid)
    url = 'https://api.weixin.qq.com/cgi-bin/tags/members/batchtagging?access_token=ACCESS_TOKEN'
    url = url.replace('ACCESS_TOKEN', ACCESS_TOKEN)
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'openid_list': [openid],
        'tagid': tagid
    }, ensure_ascii=False).encode()
    req = request.Request(url, data=data, headers=headers)
    res = request.urlopen(req)
    data = res.read().decode()
    return data
