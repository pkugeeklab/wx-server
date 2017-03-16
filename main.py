import flask
import hashlib
import xml.etree.cElementTree as ET
from template import generate
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    token = 'xuliangwei'
    signature = flask.request.args['signature']
    timestamp = flask.request.args['timestamp']
    nonce = flask.request.args['nonce']
    if 'echostr' in flask.request.args:
        echostr = flask.request.args['echostr']
        s = ''.join(sorted([token, timestamp, nonce]))
        s = s.encode()
        print('s=',s)
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
    EventKey = xml_tree.findtext('EventKey')
    print(EventKey)
    if EventKey == 'binding':
        data = generate(EventKey, {'OpenID': FromUserName, 'me': ToUserName})
        print(data.encode())
        return data
    if EventKey == 'intro':
        info = xml_tree.find('ScanCodeInfo')
        print(info.findtext('ScanType'))
        print(info.findtext('ScanResult'))
        code = info.findtext('ScanResult')
        data = generate(EventKey, {'OpenID': FromUserName, 'me': ToUserName, 'code': code })
        print(data.encode())
        return data
    return ''

if __name__ == '__main__':
    app.run()
