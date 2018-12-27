# -*- coding: utf-8 -*-
# scrapy genspider mydomain mydomain.com

import scrapy
from scrapy_splash import SplashRequest
import requests
from scrapy.selector import Selector

class MydomainSpider(scrapy.Spider):
    name = 'mydomain'
    start_urls = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=3672368498&max_behot_time=0&count=20&as=A1B54B913E11F59&cp=5B1E812F55E91E1&_signature=t6g.3xAY7MQdh39fciiJU7eoP8'

    script = '''
            function main(splash, args)
              assert(splash:go(args.url))  
              assert(splash:wait(0.5))
              return {
                html = splash:html(),
                png = splash:png(),
                har = splash:har(),
              }
            end
        '''
   
    def start_requests(self):    
        yield SplashRequest(self.start_urls, self.parse, args={'lua_source': self.script, 'wait': 0.5, 'images':0}, endpoint='execute')
        
    def parse(self, response):
        print response.text
        pass
        
        
        
        
        
        
        
            