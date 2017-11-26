# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['example.webscraping.com/']
    start_urls = ['http://example.webscraping.com//']

    def parse(self, response):
        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath('country', '//*[@id="results"]//a/text()',
                    MapCompose(unicode.strip, unicode.title))

        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        return l.load_item()
