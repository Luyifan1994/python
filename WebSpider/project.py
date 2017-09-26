import urllib2

SOURCE_URL = 'http://example.webscraping.com'
DEFAULT_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'

class LinkCrawler:

    def __init__(self):
        self.s_url = SOURCE_URL
        self.user_agent = DEFAULT_AGENT

    def download(self,headers=None):
        headers = {'user_agent': self.user_agent}
        request = urllib2.Request(self.s_url,headers=headers)
        try:
            html = urllib2.urlopen(request).read()
        except urllib2.URLError as e:
            print 'Download Error:', e.reason
