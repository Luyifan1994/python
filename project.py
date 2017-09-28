import urllib2
from bs4 import BeautifulSoup
import urlparse
import datetime
import time
import xlwt


SOURCE_URL = 'http://example.webscraping.com'
DEFAULT_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'
fields = ['country', 'area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code',
          'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours']
length = len(fields)

class Spider:

    def __init__(self, max_page=1, delay=1):
        self.headers = {'user_agent': DEFAULT_AGENT}
        self.max_page = max_page
        self.delay = delay
        self.wbk = xlwt.Workbook()
        self.sheet = self.wbk.add_sheet('country')
        for i in range(length):
            self.sheet.write(0, i, fields[i])

    def download(self, url, num_retries=2):
        print 'Downloading:', url
        request = urllib2.Request(url, headers=self.headers)
        try:
            html = urllib2.urlopen(request).read()
        except Exception as e:
            print 'Download Error:', str(e)
            html = None
            if num_retries > 0:
                if hasattr(e,'code') and 500 <= e.code < 600:
                    return self.download(url, num_retries-1)
        return html

    def link_crawler(self):
        seed_url = [SOURCE_URL]
        page = 1
        # sleep = TimeSleep(self.delay)
        while seed_url:
            url = seed_url.pop()
            time.sleep(self.delay)
            page_html = self.download(url)
            links = self.get_links(page_html)
            for nl, link in enumerate(links[:-1]):
                # time.sleep(2)
                # sleep.wait(link)
                time.sleep(self.delay)
                view_html = self.download(link)
                self.to_excel(link, view_html, nl+1,self.sheet)
                print 'Writing to excel...'
            if page < self.max_page:
                page += 1
                seed_url.append(links[-1])
        print 'Downloading Done...'

    def get_links(self, html):
        links = []
        soup = BeautifulSoup(html, 'lxml')
        for a in soup.find('div', id='results').find_all('a'):
            view_behind = a['href']
            links.append(urlparse.urljoin(SOURCE_URL, view_behind))
        index_behind = soup.find('div', id="pagination").find_all('a')[-1]['href']
        links.append(urlparse.urljoin(SOURCE_URL, index_behind))
        return links

    def to_excel(self, url, html, row, sheet):
        country = url.split('/')[-1].split('-')[0]
        # print country
        soup = BeautifulSoup(html,'lxml')
        sheet.write(row, 0, country)
        for j, f in enumerate(fields[1:-1]):
            conp = soup.select('tr#places_{}__row > td.w2p_fw'.format(f))[0].string
            if conp is None:
                conp = 'None'
            # print conp,row, j
            sheet.write(row, j+1, conp)
        neblist = soup.select('tr#places_neighbours__row > td.w2p_fw > div > a')
        neb = ''
        for n in neblist:
            neb += n.string
        sheet.write(row, length-1, neb)
        self.wbk.save('country.xls')


# class TimeSleep:
#
#     def __init__(self, delay):
#         self.delay = delay
#         self.domain = {}
#
#     def wait(self,url):
#         domain = urlparse.urlparse(url).netloc
#         last_access = self.domain.get(domain)
#         if self.delay > 0 and last_access is not None:
#             sleep_time = self.delay - (datetime.datetime.now() - last_access).seconds
#             # print sleep_time
#             if sleep_time > 0:
#                 time.sleep(sleep_time)
#         self.domain[domain] = datetime.datetime.now()


if __name__ == '__main__':
    spider = Spider()
    spider.link_crawler()





