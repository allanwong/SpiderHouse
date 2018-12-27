# -*- coding: utf-8 -*-
import json

from tutorial.items import TouTiaoMediarItem
from src.service import DataService as ds
from src.utils import DateUtils as du
import toutiao

# 针对搜索媒体号结果，媒体号目录作为数据沉淀系统中
class ToutiaoMediaUserSpider(toutiao.ToutiaoSpider):
    name = 'toutiao_media_user'
    start_urls = 'https://www.toutiao.com/search_content/?offset={num}&format=json&keyword={keywords}&autoload=true&count=20&cur_tab=4&from=media'
#   采集关键字
    keywords = "艾茸宝宝"
    media_type = '0'
    # parse the html content 
    def parse(self, response):
        self.searchInterfacePage(response)
        
    def searchInterfacePage(self, response):        
        list = response.xpath('//pre/text()').extract_first()
        arr = json.loads(list)['data']
        doc_list = []
        
        for item in arr:
            toutiaoItem = TouTiaoMediarItem()
            toutiaoItem['media_id'] = du.get_unit_id()
            toutiaoItem['media_name'] = item.get('name')
            toutiaoItem['media_type'] = self.media_type
            toutiaoItem['img_url'] = item.get('avatar_url')
            toutiaoItem['user_url'] = item.get('source_url')
            toutiaoItem['keywords'] = self.keywords
            toutiaoItem['create_time'] = du.current_time()
            toutiaoItem['remark'] = item.get('description')    
            toutiaoItem['source'] = "toutiao.com"
            
            if self.check_media(toutiaoItem) == True:
                doc_list.append(toutiaoItem)
        
        if len(doc_list) == 0:
            print '程序完成'
            self.flag = False
        else:
            ds.getToutiaoMediaUser(doc_list)    
                
    def check_media(self,toutiaoItem):        
        return True
