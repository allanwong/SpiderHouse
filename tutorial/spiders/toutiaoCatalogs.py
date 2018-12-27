# -*- coding: utf-8 -*-
import json

from tutorial.items import TouTiaoItem
from src.service import DataService as ds
from src.utils import DateUtils as du
import toutiao

# 针对搜索文章结果，文章目录作为数据沉淀系统中
class ToutiaoCatalogsSpider(toutiao.ToutiaoSpider):
    name = 'toutiao_catalogs'
    start_urls = 'https://www.toutiao.com/search_content/?offset={num}&format=json&keyword={keywords}&autoload=true&count=20&cur_tab=1&from=search_tab'
#   采集关键字
    keywords = "徐浩大夫"
    
    # parse the html content 
    def parse(self, response):
        self.searchInterfacePage(response)
        
    def searchInterfacePage(self, response):        
        list = response.xpath('//pre/text()').extract_first()
        arr = json.loads(list)['data']
        
        source = "toutiao.com"
        doc_list = []
        for item in arr:
            toutiaoItem = TouTiaoItem()
            toutiaoItem['doc_id'] = du.get_unit_id()
            toutiaoItem['doc_type'] = "1"
            toutiaoItem['sp_type'] = "1"
            toutiaoItem['abstract'] = item.get('abstract')
            toutiaoItem['article_url'] = item.get('article_url')
            toutiaoItem['comment_count'] = item.get('comment_count')
            toutiaoItem['datetime'] = item.get('datetime')
            toutiaoItem['create_time'] = du.current_time()
            toutiaoItem['image_url'] = item.get('image_url')
            toutiaoItem['keyword'] = item.get('keyword')
            toutiaoItem['media_name'] = item.get('media_name')
            toutiaoItem['source'] = source
            toutiaoItem['tag'] = item.get('tag')
            toutiaoItem['tag_id'] = item.get('tag_id')
            toutiaoItem['title'] = item.get('title')
            toutiaoItem['video_duration'] = item.get('video_duration')
            if self.check_doc(toutiaoItem):
                doc_list.append(toutiaoItem)  
#                 print('{}、{},{}'.format(toutiaoItem['doc_id'],toutiaoItem['title'],toutiaoItem['doc_id'])) 
                
        if len(doc_list) == 0:
            self.flag = False
        else:
            ds.getDocCatalogs(doc_list)    
        
    def check_doc(self,toutiaoItem):
        
        if toutiaoItem['video_duration'] != None:
            return False
        
        if toutiaoItem['title'] == None:
            return False
        
        if toutiaoItem['article_url'] == None:
            return False
        
        return True
        
    def search(self, response):
        
        content_list = response.xpath('//span[@class="J_title"]')
        count = 1
        for content in content_list:
            arr = content.xpath('.//text()').extract()
            print("{}、{}".format(count,"".join(arr) )) 
            count+=1   
                