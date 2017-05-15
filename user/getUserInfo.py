from urllib import request, parse
import json
from getAccessToken import getToken
import sys

def getUserInfo(openid):
    access_token = getToken()
    url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=ACCESS_TOKEN&openid=OPENID&lang=zh_CN '
    url = url.replace('ACCESS_TOKEN', access_token)
    url = url.replace('OPENID', openid)
    req = request.Request(url)
    res = request.urlopen(req)
    data = res.read().decode()
    userinfo = json.loads(data)
    return userinfo

if __name__ == '__main__':
    openid = sys.argv[1]
    print(getUserInfo(openid))
