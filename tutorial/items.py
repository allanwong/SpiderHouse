# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from numpy import source


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()
    desc = scrapy.Field() 
    
class TouTiaoItem(scrapy.Item):    
    doc_id = scrapy.Field() 
    doc_type = scrapy.Field() 
    sp_type = scrapy.Field() 
    abstract = scrapy.Field() 
    article_url = scrapy.Field() 
    comment_count = scrapy.Field() 
    datetime = scrapy.Field() 
    create_time = scrapy.Field() 
    image_url = scrapy.Field() 
    keyword = scrapy.Field() 
    media_id = scrapy.Field() 
    media_name = scrapy.Field() 
    source = scrapy.Field() 
    tag = scrapy.Field() 
    tag_id = scrapy.Field() 
    create_time = scrapy.Field() 
    title = scrapy.Field() 
    video_duration = scrapy.Field() 
    view_num = scrapy.Field() 
    
class TouTiaoMediarItem(scrapy.Item):    
    media_id = scrapy.Field() 
    media_name = scrapy.Field() 
    media_type = scrapy.Field() 
    source = scrapy.Field() 
    img_url = scrapy.Field() 
    user_url = scrapy.Field() 
    keywords = scrapy.Field() 
    create_time = scrapy.Field() 
    remark = scrapy.Field() 
     