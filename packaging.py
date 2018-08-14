from urllib import request, parse
from urllib.error import URLError, HTTPError
import json, hashlib
from http import cookiejar
'''
封装request
* 传入URL
* user_agent
* headers
* data
* urlopen
* 返回bytes 数组
* get or post
'''

class Session():
    def __init__(self):
        cookie_object = cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(cookie_object)
        self.opener = request.build_opener(handler)

    def get(self, url, headers=None):
        return get(url, headers,self.opener)

    def post(self, url, form, headers=None):
        return post(url, form, headers, self.opener)


def md5(key):
    # 创建一个MD5对象
    md5_a = hashlib.md5()
    # 需要有bytes, 作为参数
    # 由str, 转换成 bytes encode-------str.encode('utf-8')
    # 由bytes转换成 str, decode---------bytes.decode('utf-8')
    sign_bytes = key.encode('utf-8')
    # print(type(sign_bytes))
    # 更新md5 object的值
    md5_a.update(sign_bytes)
    sign_str = md5_a.hexdigest()
    return sign_str


def get(url, headers=None, opener=None):
    '''
    :param url: 必填,传入的Url
    :param headers: 可不填,如果用户需要自行传入headers, 则覆盖之前的headers
    :return:返回调用的urlrequest封装的方法
    '''
    return urlrequest(url, headers=headers, opener=opener)


def post(url, data, headers=None, opener=None):
    '''
    :param url: 必填, User传入的Url
    :param data: 必填, 这里为传递给服务器的参数
    :param headers:可不填
    :return:
    '''
    return urlrequest(url, data, headers=headers, opener=opener)


def urlrequest(url, data=None, headers=None, opener=None):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    html = ''
    if headers == None:
        # 如果没有传递headers 则使用默认的headers
        headers = {
            'User-Agent': user_agent
        }
    # 这里使用try, except 捕获异常, Eg: HTTPError404错误等...  和 URLError连接超时,服务器不存在,网络无连接等错误
    try:
        if data:
            # 把data 参数转成Unicode编码 (一般浏览器都是采用Unicode编码传递中文参数)
            data_str = parse.urlencode(data)
            data_bytes = data_str.encode('utf-8')
            req = request.Request(url, data=data_bytes, headers=headers)
        else:
            req = request.Request(url, headers=headers)
        if opener:
            response = opener.open(req)
        else:
            response = request.urlopen(req)
        html = response.read()
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    return html


if __name__ == '__main__':
    # url = 'http://weibo.com'
    # html = urlrequest(url).decode('gb2312')
    # print(html)
    # 测试

    url = 'http://fanyi.baidu.com/sug'
    while True:
        data = input('请输入要翻译的词语,按Q返回:')
        if data == 'q' or data == 'Q':
            break
        form = {
            'kw': data
        }
        html_bytes = post(url, data=form).decode('utf-8')
        try:
            html = json.loads(html_bytes,encoding='utf-8')['data'][0]['v']
            print('翻译:', '\n\r\r', html)
        except IndexError as e:
            print('错误:',e)

