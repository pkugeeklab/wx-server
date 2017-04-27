import json
from urllib import parse, request

from getAccessToken import getToken


def getMaterialList(kind, offset, count):
    ACCESS_TOKEN = getToken()
    url = 'https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=ACCESS_TOKEN'
    url = url.replace('ACCESS_TOKEN', ACCESS_TOKEN)
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'type': kind,
        'offset': offset,
        'count': count
    }, ensure_ascii=False).encode()
    req = request.Request(url, data=data, headers=headers)
    res = request.urlopen(req)
    data = res.read().decode()
    data = json.loads(data)
    ret = {}
    ret['count'] = data['item_count']
    ret['items'] = [{'id': item['media_id'],
                     'title': item['content']['news_item'][0]['title']}
                    for item in data['item']]
    return ret
