# -*- coding: utf-8 -*-
import json
from scrapy_splash import SplashRequest
from tutorial.items import TouTiaoItem
from src.service import DataService as ds
from src.utils import DateUtils as du
import toutiao
import re
from __builtin__ import False
# 针对媒体文章结果，更新文章作为数据沉淀系统中
class ToutiaoMediasSpider(toutiao.ToutiaoSpider):
    name = 'toutiao_medias'
    start_urls = ['http://www.toutiao.com/c/user/50748883871/']
    script = '''
        function main(splash, args)
          splash:set_viewport_size(1028,500) 
          splash.scroll_to(0,1000)
          assert(splash:go(args.url))  
          assert(splash:wait(0.5))
          return {
            html = splash:html(),
            png = splash:png(),
            har = splash:har(),
          }
        end
    '''
    
#    临时通过媒体url地址加载文章目录，需要设定参数param = {'media_id':'1529045596944061641'}
    isMediaUrl = False
    
#     是否对今天得数据加载
    isToday = True
    
    # start request    
    def start_requests(self):
#         param = {'media_id':'1529045596944061641', 'create_time':'2018-06-13 23', 'format':'%%Y-%%m-%%d %%H'}
        param = {'source':'toutiao.com'}
        media_list = []
        
        if self.isMediaUrl == True:
            for url in self.start_urls:
                yield SplashRequest(url, self.parse, meta={'media_id':param['media_id']}, args={'lua_source': self.script, 'wait': 0.5, 'images':0}, endpoint='execute')
        else:
            if self.isToday == False:#对没有加载文章目录的媒体进行数据加载
                media_list = ds.queryToutiaoMediaUserUnDone(param)
            else:
                media_list = ds.queryToutiaoMediaUser(param)#对当前的数据进行加载
                
            for media in media_list:
                yield SplashRequest(media['user_url'], self.parse, meta={'media_id':media['media_id']}, args={'lua_source': self.script, 'wait': 0.5, 'images':0}, endpoint='execute')
    
    # parse the html content 
    def parse(self, response):
        
        qlist = response.xpath('//div[@class="relatedFeed"]/ul/li/div')
        media_name = response.xpath('//div[@class="yheader"]/div/ul/li/a/span[1]//text()').extract_first()
        
        media_id=response.meta['media_id']  
        
        doc_list = []
        for item in qlist:
            title = item.css('div.title-box').xpath('./a/text()').extract_first()
            article_url = item.css('div.title-box').xpath('./a/@href').extract_first()
            view_num = item.css('div.y-left').xpath('./a[1]/text()').extract_first() 
            comment_count = item.css('div.y-left').xpath('./a[2]/text()').extract_first() 
            date_time = item.css('div.y-left').xpath('./span//text()').extract() 
            img_url = item.css('div.lbox').xpath('./a/img/@src').extract_first()
             
            if len(date_time) == 2:
                date_time = date_time[1]
            else:
                date_time = date_time[0]    
                
            date_time = date_time.replace('⋅ ','')
            curr_time = du.current_time()
            
            if self.isToday and du.is_current_fdate(date_time, '%Y-%m-%d %H:%M') == False:
                continue
            
            toutiaoItem = TouTiaoItem()
            toutiaoItem['doc_id'] = du.get_unit_id()
            toutiaoItem['doc_type'] = "1"
            toutiaoItem['sp_type'] = "2"
            toutiaoItem['datetime'] = date_time
            toutiaoItem['create_time'] = curr_time
            toutiaoItem['image_url'] = img_url
            toutiaoItem['media_name'] = media_name
            toutiaoItem['media_id'] = media_id
            toutiaoItem['source'] = "toutiao.com"
            toutiaoItem['title'] = title
            
            if float(comment_count.replace('评论','').replace(' ','')) > 0 :
                toutiaoItem['comment_count'] = float(comment_count.replace('评论','').replace(' ',''))
            else:
                toutiaoItem['comment_count'] = '0.0'  
            
            
            if '播放' in view_num:
                continue
            
            f_view_num = float(re.sub('[^\d.]', '', view_num))
            
            if f_view_num > 0 :     
                if '万' in view_num:
                    toutiaoItem['view_num'] = f_view_num*10000
                else:
                    toutiaoItem['view_num'] = f_view_num
            else:
                toutiaoItem['view_num'] = '0.0'  
                
            toutiaoItem['article_url'] = article_url
            doc_list.append(toutiaoItem)  
        
        if len(doc_list) == 0:
            print("Any documents found from media({})".format(media_id)) 
        else:
            ds.getMediaCatalogs(doc_list)        
        
        
        