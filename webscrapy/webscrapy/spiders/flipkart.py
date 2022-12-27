import scrapy
from ..items import WebscrapyItem
 # to run the flipkart spider open the terminal cd and then run -scrapy crawl flipkart and the result should be saved to flipkart.csv
class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2']

    def parse(self, response):
        items = WebscrapyItem()
        products = response.xpath('//*[@class="_3pLy-c row"]')
        for p in products: 
            items['product_name'] = p.xpath('.//*[@class="_4rR01T"]/text()').extract_first()
            items['product_price'] = p.xpath('.//*[@class="_30jeq3 _1_WHN1"]/text()').extract_first()
            items['product_rate'] = p.xpath('.//*[@class="_3LWZlK"]/text()').extract_first()
            yield items