# coding:utf-8
# 获取一个网站的html文件

import urllib2
import zlib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'


def load(url,retry=2):
    header = {'user_agent': user_agent, 'Accept-encoding': 'gzip'}
    print 'Downloading from:' + url
    request = urllib2.Request(url,headers=header)
    try:
        response = urllib2.urlopen(request)
        html = response.read()
        info = response.info()
        if info.get('Content-Encoding') == 'gzip':
            html = zlib.decompress(html, 16+zlib.MAX_WBITS)
    except Exception as e:
        html = None
        print 'Download Error:', str(e)
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return load(url, retry - 1)
    return html


if __name__ == '__main__':
    urls = raw_input('Input url:')
    res = load(urls)
    with open('data.xml','w') as f:
        f.write(res)
