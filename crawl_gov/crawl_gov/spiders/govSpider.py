import scrapy
import logging
from crawl_gov.items import Item

class GovspiderSpider(scrapy.Spider):
    name = 'govSpider'
    allowed_domains = ['gov.bg']
    start_urls = ['https://gov.bg/bg/prestsentar/novini?page=1']

    def extractInfo(self, response):
        item = Item()
        item = {
                "title": response.css('div.container > div.row > div.col-lg-12.view > h1').get(),
                "desc": response.xpath('div.container > div.row > div.col-lg-12.view > p').get(),
                "imgLink": response.xpath('div.container > div.row > div.col-lg-12.view > div.gallery > div.lSSlideOuter > div.lSSlideWrapper.usingCss > ul.lightSlider.lSSlide > li.lslide.active > img::attr(src)').get()
        }

        yield item


    def parse(self, response):
        logging.getLogger('scrapy').propagate = False
        for href in response.css("div.container > div.row > div.col-lg-12 > div.articles > div.item.no-padding > div.col-lg-5 > a::attr(href)").get():
            yield scrapy.Request(href, callback=self.extractInfo) 
