# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from properties.items import PropertiesItem
from scrapy.http import FormRequest


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['douban.com']

    # Start with a login request
    def start_requests(self):
        return [
            FormRequest(
                "https://accounts.douban.com/login?source=movie",
                formdata={"form_email": "457928426@qq.com", "form_password": "123qweasd"}
            )]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[text()="Next >"]'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath('country', '//*[@id="results"]//a/text()',
                    MapCompose(unicode.strip, unicode.title))

        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        return l.load_item()
