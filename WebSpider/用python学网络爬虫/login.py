# coding:utf-8

import urllib2, urllib
import cookielib
from bs4 import BeautifulSoup

LOGIN_URL = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'
LOGIN_EMAIL = '457928426@qq.com'
LOGIN_PASSWORD = 'qweasdzxc'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'


def parse_form(html):
    """extract all input properties from the form
    """
    soup = BeautifulSoup(html, 'lxml')
    data = {}
    for e in soup.find_all('input')[:-1]:
        # print e
        try:
            data[e['name']] = e['value']
        except KeyError:
            continue
    return data


header = {'user_agent': user_agent}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
html = opener.open(LOGIN_URL).read()
data = parse_form(html)

data['email'] = LOGIN_EMAIL
data['password'] = LOGIN_PASSWORD
print data
encoded_data = urllib.urlencode(data)
request = urllib2.Request(LOGIN_URL, data=encoded_data, headers=header)
response = opener.open(request)
print response.geturl()
