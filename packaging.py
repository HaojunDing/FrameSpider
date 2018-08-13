from urllib import request, parse
from urllib.error import URLError, HTTPError

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


def get(url, headers=None):
    return urlrequest(url, headers=headers)


def post(url, data, headers=None):
    return urlrequest(url, data, headers=headers)


def urlrequest(url, data=None, headers=None):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    html = ''
    if headers == None:
        headers = {
            'User-Agent': user_agent
        }
    try:
        if data:
            data_str = parse.urlencode(data)
            data_bytes = data_str.encode('utf-8')
            req = request.Request(url, data=data_bytes, headers=headers)
        else:
            req = request.Request(url, headers=headers)
        html = request.urlopen(req).read()
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    return html


if __name__ == '__main__':
    # url = 'http://weibo.com'
    # html = urlrequest(url).decode('gb2312')
    # print(html)

    url = 'http://fanyi.baidu.com/v2transapi'
    form = {
        'from':'zh',
        'to': 'en',
        'transtype':'realtime',
        'simple_means_flag': 3,
        'sign': 974510.671135,
        'token':'3578969812c56c99e14295d42a6207d5',
        'query': '丁豪俊真帅'
    }
    html_bytes = post(url, data=form)
    print(html_bytes)