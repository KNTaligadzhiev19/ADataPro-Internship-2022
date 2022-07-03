import scrapy


class GovspiderSpider(scrapy.Spider):
    name = 'govSpider'
    allowed_domains = ['gov.bg']
    start_urls = ['http://gov.bg/']

    def parse(self, response):
        pass
