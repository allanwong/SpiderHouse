#coding=utf-8 
'''
Created on 2018年4月24日

@author: bingqiw
'''
import MySQLdb as md
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

# 生产
doc_db_con =  md.connect(host='127.0.0.1', port=3306,user='root', passwd='123456', db='doc_db', charset='utf8')

def qry_sql(con,sql):
    df = pd.read_sql(sql, con=con) 
    print "Execute:"+sql
    return df

def select(con,sql, param):
    
    cur = con.cursor(cursorclass = md.cursors.DictCursor)
    print sql
    print param
    reCout = cur.execute(sql, param)
    print('data done size:{}'.format(reCout)) 
    arr = cur.fetchall()
    result = []
    for i in arr:
        result.append(i)
        
    con.commit()
    cur.close()
    return result

def execute(con, sql, param):
    cur = con.cursor()
    print sql
    print param
    reCout = cur.execute(sql, param)
    print('data done size:{}'.format(reCout)) 
    con.commit()
    cur.close()
    return reCout

def batch_sql(con, sql, param_list):    
    cur = con.cursor()
    print "sql=",sql
    print "param_list=", param_list
    reCout = cur.executemany(sql, param_list)
    print('data done size:{}'.format(reCout)) 
    con.commit()
    cur.close()
    return reCout
    
    