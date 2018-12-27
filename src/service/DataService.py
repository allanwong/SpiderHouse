#coding=utf-8 
'''
Created on 2018年4月24日

@author: bingqiw
'''
import src.datasource.DBManager as db

# 查询文章目录
# param为字典类型数据
def queryDocCatalogs(param, con=db.doc_db_con):
    sql = "select t.doc_id, t.source, t.doc_type, t.sp_type, t.title, t.abstract, t.article_url, t.image_url, t.comment_count, t.datetime, t.create_time, t.keyword, t.media_name, t.tag, t.tag_id from sp_doc_catalogs t"
    cond = " where 1=1 "
    
    result = []
    if param and len(param)>0:
        arr = []
        
        isCond = False
        
        if 'source' in param.keys() :
            arr.append(param['source'])
            cond += " and t.source=%s "
            isCond = True
            
        if 'create_time' in param.keys():
            arr.append(param['create_time'])
            cond += " and date_format(t.create_time,'"+param['format']+"')=%s "
            isCond = True
        
        if 'doc_id' in param.keys() :
            arr.append(param['doc_id'])
            cond += " and t.doc_id=%s "
            isCond = True
            
        if isCond :
            sql += cond
        
        result = db.select(con, sql, arr)
    else:
        print 'param is none, service quit !!!'    
    
    return result

# 查询没有内容的目录
def queryDocCatalogsWithoutText(param, con=db.doc_db_con):
    sql = "select t.*  from sp_doc_catalogs t "
    cond = " where t.MEDIA_ID IS NOT NULL AND t.doc_id not in (select distinct doc_id from sp_doc_passages) "
    result = []
    arr = []
    if param and len(param)>0:
        isCond = False
        
        if 'media_name' in param.keys() :
            arr.append(param['source'])
            cond += " and t.media_name=%s "
            isCond = True
            
        if 'create_time' in param.keys():
            arr.append(param['create_time'])
            cond += " and date_format(t.create_time,'"+param['format']+"')=%s "
            isCond = True
        
        if 'doc_id' in param.keys() :
            arr.append(param['doc_id'])
            cond += " and t.doc_id=%s "
            isCond = True
            
        if isCond :
            sql += cond
    else:
        print 'param is none'    
        sql += cond
        
    result = db.select(con, sql, arr)
    return result
# 抓取文章段落
def getDocPassages(doc_list, con=db.doc_db_con):
    sql = "insert sp_doc_passages (psg_id, doc_id, psg_order, psg_content, create_time, psg_keywords) VALUES (%s,%s,%s,%s,%s,%s)" 
           
    arr = []
     
    for doc in doc_list:
        arr.append([doc['psg_id'],doc['doc_id'],doc['psg_order'],doc['psg_content'],doc['create_time'],doc['psg_keywords']])
        
    flag = db.batch_sql(con,sql,arr)
    print "入库完毕"
    return flag        
    
# 根据搜索，抓取文章目录
def getDocCatalogs(doc_list, con=db.doc_db_con):
    
    sql = '''
    insert sp_doc_catalogs
    (doc_id,source,doc_type,sp_type,title,abstract,article_url,image_url,comment_count,datetime,create_time,keyword,media_name,tag,tag_id) VALUES 
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)    
    '''
    arr = []
     
    for doc in doc_list:
        arr.append([doc['doc_id'],doc['source'],doc['doc_type'],doc['sp_type'],doc['title'],doc['abstract'],doc['article_url'],doc['image_url'],doc['comment_count'],doc['datetime'],doc['create_time'],doc['keyword'],doc['media_name'],doc['tag'], doc['tag_id']])
        
#         print arr
    flag = db.batch_sql(con,sql,arr)
    print "入库完毕"
    return flag      
  
#   根据媒体号，抓取文章目录
def getMediaCatalogs(doc_list, con=db.doc_db_con):
    
    sql = '''
    insert sp_doc_catalogs
    (doc_id, source, doc_type, sp_type, title, article_url, image_url, view_num, comment_count, datetime, create_time, media_name, media_id) VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)    
    '''
    arr = []
     
    for doc in doc_list:
        arr.append([doc['doc_id'],doc['source'],doc['doc_type'],doc['sp_type'],doc['title'],doc['article_url'],doc['image_url'],doc['view_num'],doc['comment_count'],doc['datetime'],doc['create_time'],doc['media_name'],doc['media_id']])
        
#         print arr
    flag = db.batch_sql(con,sql,arr)
    print "入库完毕"
    return flag    

#通过搜索结果，得到媒体号
def getToutiaoMediaUser(doc_list, con=db.doc_db_con):
    
    sql = "insert sp_media_user (media_id, media_name, media_type, source, img_url, user_url, keywords, create_time, remark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    arr = []
     
    for doc in doc_list:
        arr.append([doc['media_id'],doc['media_name'],doc['media_type'],doc['source'],doc['img_url'],doc['user_url'],doc['keywords'],doc['create_time'],doc['remark']])
        
#         print arr
    flag = db.batch_sql(con,sql,arr)
    print "入库完毕"
    return flag             

# param为字典类型数据
# 查询头条的媒体号
def queryToutiaoMediaUser(param, con=db.doc_db_con):
    sql = "select t.media_id, t.media_name, t.source, t.img_url, t.user_url, t.keywords, t.create_time, t.remark from sp_media_user t"
    cond = " where t.media_type='0' "
    
    result = []
    if param and len(param)>0:
        arr = []
        
        isCond = False
        
        if 'source' in param.keys() :
            arr.append(param['source'])
            cond += " and t.source=%s "
            isCond = True
            
        if 'create_time' in param.keys():
            arr.append(param['create_time'])
            cond += " and date_format(t.create_time,'"+param['format']+"')=%s "
            isCond = True
        
        if 'media_id' in param.keys() :
            arr.append(param['media_id'])
            cond += " and t.media_id=%s "
            isCond = True
        
        if 'media_name' in param.keys() :
            arr.append(param['media_name'])
            cond += " and t.media_name=%s "
            isCond = True
                
        if isCond :
            sql += cond
        
        result = db.select(con, sql, arr)
    else:
        print 'param is none, service quit !!!'    
    
    return result

# 查询没有导入目录的媒体号
def queryToutiaoMediaUserUnDone(param, con=db.doc_db_con):
    sql = "select t.* from sp_media_user t  "
    cond = " where t.media_type='0' and t.media_id not in (select distinct media_id from sp_doc_catalogs where media_id is not null) "
    
    result = []
    if param and len(param)>0:
        arr = []
        
        isCond = False
        
        if 'source' in param.keys() :
            arr.append(param['source'])
            cond += " and t.source=%s "
            isCond = True
            
        if 'create_time' in param.keys():
            arr.append(param['create_time'])
            cond += " and date_format(t.create_time,'"+param['format']+"')=%s "
            isCond = True
        
        if 'media_id' in param.keys() :
            arr.append(param['media_id'])
            cond += " and t.media_id=%s "
            isCond = True
        
        if 'media_name' in param.keys() :
            arr.append(param['media_name'])
            cond += " and t.media_name=%s "
            isCond = True
                
        if isCond :
            sql += cond
        
        result = db.select(con, sql, arr)
    else:
        print 'param is none, service quit !!!'    
    
    return result
    

def queryMediaParseConf(media_id, source, con=db.doc_db_con):
    sql = "SELECT T.* FROM sp_media_sub_parse_config T WHERE T.media_id = %s union all  SELECT T.* FROM sp_media_sup_parse_config T WHERE T.media_id = %s"
    
    param = [media_id,source]
    
    result = []
    if param and len(param)>0:
        result = db.select(con, sql, param)
    else:
        print 'param is none, service quit !!!'    
    
    return result
