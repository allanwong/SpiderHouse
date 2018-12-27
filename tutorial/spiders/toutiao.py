# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from src.service import DataService as ds

class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['www.toutiao.com']
    start_urls = ''
    
#     媒体号文章内容解析模版
    media_parse_config = {}
    
#   采集关键字
    keywords = ""
    
#   媒体类型：0=抓取媒体；1=搜索媒体
    media_type = "0"
    
#   是否进行抓取数据
    flag = True
    
#   采集步长
    step = 20
    
#     是否查询今天数据
    isToday = True
    
#   根据媒体号URL查询直接
    isMediaUrl = False
    
    # start request    
    def start_requests(self):
        count = 0
        self.start_urls = self.start_urls.replace('{keywords}', self.keywords)
        while self.flag:
            url = self.start_urls.replace('{num}', str(count))
            count += self.step
            yield SplashRequest(url, self.parse, args={'wait': 3}, endpoint='render.html')
            
    # parse the html content 
    def parse(self, response):
        pass

# 解析文章的段落
    def parsePsgCnt(self, response, parse_type):
        arr = []
        
#       直接解析：
        media_id = response.meta['media_id']
        source = response.meta['source']
        doc_id = response.meta['doc_id'] 
        if media_id is None:
            return arr
        
        config = self.media_parse_config.get(media_id)
        
        if config is None or len(config) == 0:
            config = ds.queryMediaParseConf(media_id, source)
            if config is not None:  
                self.media_parse_config[media_id] = config
                
                for item in config:
                    if item['parse_type'] == parse_type:
                        arr = response.css(item['parse_slot']).xpath('.//text()').extract()
                        if len(arr) > 0:
                            break
            else:
                print 'media config not found:', media_id
        else:
            
            for item in config:
                if item['parse_type'] == parse_type:
                    arr = response.css(item['parse_slot']).xpath('.//text()').extract()
                    if len(arr) > 0:
                        break
                
            
        print '解析配置结果！arr',len(arr),'解析类型parse_type=',parse_type,'目录文章doc_id=',doc_id
        return arr
    
#         keyword = response.css('ul.tag-list li a::text').extract()
#         keyword = ','.join(keyword)
        
#         arr = response.css('div.article-content div p').xpath('.//text()').extract()
#         
#         if len(arr) == 0 :
#             arr = response.css('div.article-content p').xpath('.//text()').extract()
#         
#         if len(arr) == 0 :
#             arr = response.css('div.abstract').xpath('.//text()').extract()
#             
#         if len(arr) == 0 :
#             arr = response.css('div.article-content h1').xpath('.//text()').extract()
#             
#         if len(arr) == 0 :
#             print '解析结果为空！',response.css('div.article-content').xpath('.//text()').extract()