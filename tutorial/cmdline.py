#coding=utf-8 
'''
Created on 2018年6月2日

@author: bingqiw
'''
import scrapy.cmdline  
  
if __name__ == '__main__':  
    
    scrapy.cmdline.execute(argv=['scrapy','crawl','toutiao_medias'])  
#     scrapy.cmdline.execute(argv=['scrapy','crawl','toutiao_test'])  
#     scrapy.cmdline.execute(argv=['scrapy','crawl','toutiao_media_user']) 
#     scrapy.cmdline.execute(argv=['scrapy','crawl','toutiao_catalogs'])  
#     scrapy.cmdline.execute(argv=['scrapy','crawl','toutiao_content'])  
