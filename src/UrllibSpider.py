#coding=utf-8 
'''
Created on 2018年6月1日

@author: bingqiw
'''
# 利用urllib库进行网络抓取
import urllib
import urllib2

def getDataByGETFromURLLib():
    response = urllib.urlopen('http://www.baidu.com')
    print(response.read().decode('utf-8'))
        
def getDataByPOSTFromURLLib():
    data = bytes(urllib.urlencode({'word': u'我们'}))
    print(data)

    response = urllib.urlopen('http://httpbin.org/post', data=data)
    print(response.read())    

def getDataByRequest(): 
    url = 'http://httpbin.org/post'
    dict = {
        'name': u'我们'
    }
    data = bytes(urllib.urlencode(dict))
    req = urllib2.Request(url=url, data=data)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    response = urllib2.urlopen(req)
    print(response.read().decode('utf-8'))
 
if __name__ == '__main__':
    
    getDataByRequest()
    
    
    
           