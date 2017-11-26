# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader


class BaiduSpider(scrapy.Spider):
    name = 'baidu'

    def start_requests(self):
        wd = '电影'
        return [Request('https://www.baidu.com/s?wd=%s' % wd, callback=self.parse)]

    def parse(self, response):
        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath('title', '//*[@id="rs"]//a/text()')
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)

        return l.load_item()
