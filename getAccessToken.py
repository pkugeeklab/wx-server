from urllib import request
import os
import time
import json

APPID = 'wxfcaf6f0171c0479b'
APPSECRET = 'e435add6f446c3cd9b474ed15c5a36a3'
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET'
url = url.replace('APPID', APPID)
url = url.replace('APPSECRET', APPSECRET)

def getToken():
    token = None
    print(os.path.getctime('token') - time.time())
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
    print(Atoken)
