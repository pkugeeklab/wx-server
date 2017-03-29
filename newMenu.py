from urllib import request, parse
import json
from getAccessToken import getToken
ACCESS_TOKEN = getToken()

url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token=ACCESS_TOKEN'
url = url.replace('ACCESS_TOKEN', ACCESS_TOKEN)
req = request.Request(url)
res = request.urlopen(req)
data = res.read().decode()
print(data)


url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN'
url = url.replace('ACCESS_TOKEN', ACCESS_TOKEN)
headers = {
    'Content-Type': 'application/json'
}
data = json.load(open('menu_common.json', 'r'))

data = json.dumps(data, ensure_ascii=False).encode()
req = request.Request(url, data=data, headers=headers)
res = request.urlopen(req)
data = res.read().decode()
print(data)
