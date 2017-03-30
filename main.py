import hashlib
import xml.etree.cElementTree as ET

import flask
import pymongo

from template import generate
from secret import *
app = flask.Flask(__name__)
client = pymongo.MongoClient('localhost', 27017)
db = client['geeklab']
items = db['items']


@app.route('/', methods=['GET'])
def main():
    signature = flask.request.args['signature']
    timestamp = flask.request.args['timestamp']
    nonce = flask.request.args['nonce']
    if 'echostr' in flask.request.args:
        echostr = flask.request.args['echostr']
        s = ''.join(sorted([Token, timestamp, nonce]))
        s = s.encode()
        print('s=', s)
        r = hashlib.sha1(s)
        r = r.hexdigest()
        print(r)
        if r == signature:
            return echostr
    return ''


@app.route('/', methods=['POST'])
def reply():
    data = flask.request.values
    signature = flask.request.args['signature']
    timestamp = flask.request.args['timestamp']
    nonce = flask.request.args['nonce']
    # print(dir(flask.request))
    print(flask.request.data)
    xml_tree = ET.fromstring(flask.request.data)

    FromUserName = xml_tree.findtext('FromUserName')
    print(FromUserName)
    ToUserName = xml_tree.findtext('ToUserName')
    Event = xml_tree.findtext('Event')
    EventKey = xml_tree.findtext('EventKey')
    print(Event, EventKey)
    if Event == 'subscribe':
        data = generate({'OpenID': FromUserName,
                       'me': ToUserName,
                       'text', '欢迎关注哦！北大小极为您服务~'}, EventKey)
        return data
    else:
        if EventKey == 'binding':
            data = generate({'OpenID': FromUserName, 'me': ToUserName}, EventKey)
            print(data.encode())
            return data
        elif EventKey == 'intro':
            info = xml_tree.find('ScanCodeInfo')
            print(info.findtext('ScanType'))
            print(info.findtext('ScanResult'))
            code = info.findtext('ScanResult')
            if code:
                item = items.find_one({'code': code[1:]})
                if item:
                    description = item['description']
                else:
                    description = 'No description'
                data = generate({'OpenID': FromUserName,
                               'me': ToUserName,
                               'code': code,
                               'description': description}, EventKey)
                print(data)
                return data
            else:
                return ''
        else:
            data = generate({'OpenID': FromUserName,
                           'me': ToUserName}, EventKey)
            return data
    return ''


if __name__ == '__main__':
    app.run(debug=True)
