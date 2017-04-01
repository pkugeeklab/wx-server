from urllib import request, parse
import json
from getAccessToken import getToken


def getUserlist():
    ACCESS_TOKEN = getToken()
    url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&next_openid='
    url = url.replace('ACCESS_TOKEN', ACCESS_TOKEN)
    req = request.Request(url)
    res = request.urlopen(req)
    data = res.read().decode()
    return data
