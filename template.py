import time
NEWS = '''
<xml>
    <ToUserName><![CDATA[%(OpenID)s]]></ToUserName>
    <FromUserName><![CDATA[%(me)s]]></FromUserName>
    <CreateTime>%(CreateTime)s</CreateTime>
    <MsgType><![CDATA[news]]></MsgType>
    <ArticleCount>1</ArticleCount>
    <Articles>
        <item>
            <Title><![CDATA[%(Title)s]]></Title>
            <Description><![CDATA[%(Description)s]]></Description>
            <Url><![CDATA[%(Url)s]]></Url>
        </item>
    </Articles>
</xml>
'''

TEXT = '''
<xml>
    <ToUserName><![CDATA[%(OpenID)s]]></ToUserName>
    <FromUserName><![CDATA[%(me)s]]></FromUserName>
    <CreateTime>%(CreateTime)s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%(Text)s]]></Content>
</xml>
'''


def generate(data, key=None, msgType=None):
    if key == 'binding':
        valueDict = {
            'OpenID': data['OpenID'],
            'me': data['me'],
            'CreateTime': int(time.time()),
            'Title': '绑定',
            'Description': '点击跳往绑定页面',
            'Url': 'http://www.baidu.com/s?wd=%s' % data['OpenID']
        }
        msgType = NEWS if not msgType else msgType
        return NEWS % valueDict
    elif key == 'intro':
        valueDict = {
            'OpenID': data['OpenID'],
            'me': data['me'],
            'CreateTime': int(time.time()),
            'Text': data['description'] + data['code']
        }
        msgType = TEXT if not msgType else msgType
        return TEXT % valueDict
    else:
        valueDict = {
            'OpenID': data['OpenID'],
            'me': data['me'],
            'CreateTime': int(time.time()),
            'Text': '功能开发中，敬请期待~'
        }
        return TEXT % valueDict
