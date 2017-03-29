from urllib import request
import os
import time
import json
from secret import *
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=AppID&secret=AppSecret'
url = url.replace('AppID', AppID)
url = url.replace('AppSecret', AppSecret)


def getToken():
    token = None
    if os.path.exists('token') and time.time() - os.path.getctime('token') < 7000:
        token = open('token', 'r').readline().strip()
    else:
        req = request.urlopen(url)
        data = req.read().decode()
        data = json.loads(data)
        print(data)
        if 'access_token' in data:
            token = data['access_token']
            open('token', 'w').write(token)
    return token


if __name__ == '__main__':
    Atoken = getToken()
    assert Atoken
    print(Atoken)
