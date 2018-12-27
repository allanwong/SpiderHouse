# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['http://books.toscrape.com/']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        
        try:
            
            for book in response.css('article.product_pod'):
                items = TutorialItem()
                
                #抓取商品名称
                items['name'] = book.xpath('./h3/a/@title').extract_first()
                
                #抓取商品价格
                #price = book.xpath('./div[2]/p[1]/text()').extract_first()
                items['price'] = book.css('p.price_color::text').extract_first()
                
                #抓取商品链接
                href = book.xpath('./div[1]/a/@href').extract_first()
                href = response.urljoin(href)
                items['href'] = href
                
                yield scrapy.Request(url=href,meta={'items':items},callback=self.pare_detail,dont_filter=True)  
            
        except BaseException, err: 
            print(err)
    
    def pare_detail(self, response):
        
        items=response.meta['items']  
        items['desc']=response.xpath('//article[@class="product_page"]/p/text()').extract_first()
        yield items  
             