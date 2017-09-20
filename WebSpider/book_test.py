import urllib2
import re
import itertools

def download(url, user_agent = 'wswp', num_retrises = 2):
    print 'Downloading:' + url
    headers = {'user_agent': user_agent}
    request = urllib2.Request(url,headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download Error:', e.reason
        html = None
        if num_retrises > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retrises-1)
    return html

def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)

def iterid(url):
    max_error = 5
    num_error = 0
    for page in itertools.count(1):
        purl = url + '/%s' % str(page)
        html = download(purl)
        if html is None:
            num_error += 1
            if num_error == max_error:
                break
        else:
            num_error = 0

def get_links(html):
    webpage_regex = re.compile('href="(.+?)">')
    res = webpage_regex.findall(html)
    return res


# iterid('http://example.webscraping.com/places/default/view')
# print crawl_sitemap('http://example.webscraping.com/sitemap.xml')
# url = r'http://httpstat.us/500'
# print download(url)