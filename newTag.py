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
data = {
     "button":[
     {
        "name":"用户",
        "sub_button": [
            {
              "type": "click",
              "name": "绑定",
              "key": "binding"
            },
            {
              "type": "view",
              "name": "解绑",
              "url": "http://www.pku.edu.cn/"
            },
            {
              "type": "view",
              "name": "我的资料",
              "url": "http://www.pku.edu.cn/"
            }]
    },
     {
            "name": "预约",
            "sub_button": [
                {
                    "type": "view",
                    "name": "开始预约",
                    "url": "http://www.pku.edu.cn/",
                },
                {
                    "type": "click",
                    "name": "我的预约",
                    "key": "rselfmenu_0_1",
                }]
        },
      {
           "name":"更多功能",
           "sub_button":[
           {
               "type":"scancode_waitmsg",
               "name":"设备介绍",
               "key": "intro",
               "sub_button": []
            },
            {
               "type":"view",
               "name":"实验室介绍",
               "url":"http://v.qq.com/"
            },
            {
               "type":"click",
               "name":"联系我们",
               "key":"V1001_GOOD"
            }]
       }]
 }

data = json.dumps(data,ensure_ascii=False).encode()
req = request.Request(url, data=data, headers=headers)
res = request.urlopen(req)
data = res.read().decode()
print(data)
