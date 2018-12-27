# -*- coding: utf-8 -*-
import json
from scrapy_splash import SplashRequest
from tutorial.items import TouTiaoItem
from src.service import DataService as ds
from src.utils import DateUtils as du
import toutiao

# 针对搜索文章结果，文章目录作为数据沉淀系统中
class ToutiaoTestSpider(toutiao.ToutiaoSpider):
    name = 'toutiao_test'
    start_urls = 'https://www.toutiao.com/c/user/50748883871/#mid=51019986798'

#   采集关键字
    keywords = "徐浩大夫"
    
    script = '''
        function main(splash, args)
          assert(splash:autoload("https://code.jquery.com/jquery-3.3.1.min.js"))
          assert(splash:go(args.url))
          assert(splash:runjs("$('span.name').html(TAC.sign('507488838711527759887'))"))
          assert(splash:wait(0.5))
          return {
            html = splash:html(),
            png = splash:png(),
            har = splash:har(),
            toutiao_flag = splash:runjs("TAC.sign('507488838711527759887')")
      }
        end
    '''
    
    def start_requests(self):
        yield SplashRequest(self.start_urls, self.parse, args={'lua_source': self.script, 'wait': 0.5, 'images':0}, endpoint='execute')
    
    # parse the html content 
    def parse(self, response):
        print response.text
        list = response.xpath('//pre/text()').extract_first()
        arr = json.loads(list)['data']
        for item in arr:
            print item['title'], item['behot_time']
        
    
                