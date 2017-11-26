# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ["github.com"]
    start_urls = ['https://github.com/']

    # post_headers = {
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    #     "Cache-Control": "no-cache",
    #     "Connection": "keep-alive",
    #     "Content-Type": "application/x-www-form-urlencoded",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
    #     "Referer": "https://github.com/",
    # }

    def start_requests(self):
        return [Request("https://github.com/login", meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        return [FormRequest.from_response(response,url='https://github.com/session',
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          # headers=self.post_headers,
                                          formdata={'login': '457928426@qq.com', 'password': '123qweasd',
                                                    'authenticity_token':authenticity_token},
                                          callback=self.parse,
                                          dont_filter=True)]

    def parse(self, response):
        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath('title', '//span[@class="repo"]/text()')
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        return l.load_item()