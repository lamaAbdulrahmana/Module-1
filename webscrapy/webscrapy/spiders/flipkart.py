import scrapy
from ..items import WebscrapyItem

class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2']

    def parse(self, response):
        items = WebscrapyItem()
        for p in response.xpath('//div[@class="_13oc-S"]'):
            items['product_name'] = p.xpath("//div[@class='_2kHMtA']//div[@class='_4rR01T']/text()").extract()
            items['product_price'] = p.xpath("//div[@class='_2kHMtA']//div[@class='_30jeq3 _1_WHN1']/text()").extract()
            items['product_rate'] = p.xpath("//div[@class='_2kHMtA']//div[@class='_3LWZlK']/text()").extract()
            print(items)
            yield items