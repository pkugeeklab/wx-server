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


def generate(key, data):
    if key == 'binding':
        valueDict = {
            'OpenID': data['OpenID'],
            'me': data['me'],
            'CreateTime': int(time.time()),
            'Title': '绑定',
            'Description': '点击跳往绑定页面',
            'Url': 'http://www.baidu.com/s?wd=%s' % data['OpenID']
            }
        return NEWS % valueDict
    elif key == 'intro':
        valueDict = {
            'OpenID': data['OpenID'],
            'me': data['me'],
            'CreateTime': int(time.time()),
            'Title': data['code'],
            'Description': '点击跳往绑定页面',
            'Url': 'http://www.baidu.com/s?wd=%s' % data['code']
            }
        return NEWS % valueDict
