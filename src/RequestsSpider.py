#coding=utf-8 
'''
Created on 2018年6月1日

@author: bingqiw
'''
# 利用requests库进行网络抓取
import requests

def demo():
    response  = requests.get("https://www.baidu.com")
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)
    print(response.content)
    print(response.content.decode("utf-8"))
    
def demo2(): 
#     requests.post("http://httpbin.org/post")
#     requests.put("http://httpbin.org/put")
#     requests.delete("http://httpbin.org/delete")
#     requests.head("http://httpbin.org/get")
#     requests.options("http://httpbin.org/get")
    
#     get method
#     response = requests.get("http://httpbin.org/get?name=zhaofan&age=23")
#     print(response.text)
    
    data = {
        "name":"zhaofan",
        "age":22
    }
    response = requests.get("http://httpbin.org/get",params=data)
    print(response.url)
    print(response.text)
    
    data = {
        "name":"zhaofan",
        "age":23
    }
    response = requests.post("http://httpbin.org/post",data=data)
    print(response.text)


import json

def demo3():
    response = requests.get("http://httpbin.org/get")
    print(type(response.text))
    print(response.json())
    print(json.loads(response.text))
    print(type(response.json()))
    print("从结果可以看出requests里面集成的json其实就是执行了json.loads()方法，两者的结果是一样的")

def demo4():
#     response =requests.get("https://www.zhihu.com")
#     print(response.text)
#     上边会报错
#     <head><title>400 Bad Request</title></head>
#     <body bgcolor="white">
#     <center><h1>400 Bad Request</h1></center>
#     <hr><center>openresty</center>
#     </body>
#     </html>

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    
    response =requests.get("https://www.zhihu.com",headers=headers)
    print(response.text)

from lxml import etree
import urllib2,urllib
global count
def demo5():
    
    url = 'https://www.toutiao.com/ch/news_regimen/'
    try:
        headers = {
            'Host': 'www.toutiao.com',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
            'Connection': 'Keep-Alive',
            'Content-Type': 'text/plain; Charset=UTF-8',
            'Accept': '*/*',
            'Accept-Language': 'zh-cn',
            'cookie':'__tasessionId=u690hhtp21501983729114;cp=59861769FA4FFE1'}
        response = requests.get(url,headers = headers)
#         print response.status_code
        
        html = response.content
        print html
        tree = etree.HTML(html)
         
        title = tree.xpath('//a[@class="link title"]/text()')
        source = tree.xpath('//a[@class="lbtn source"]/text()')
        comment = tree.xpath('//a[@class="lbtn comment"]/text()')
        stime = tree.xpath('//span[@class="lbtn"]/text()')
#         print len(title)   #0
#         print type(title)  #<type 'list'>    
        for x,y,z,q in zip(title,source,comment,stime):
            count += 1
            data = {
                'title':x.text,
                'source':y.text,
                'comment':z.text,
                'stime':q.text}
            print count,'|',data
            
    except urllib2.URLError, e:
        print e.reason    

from bs4 import BeautifulSoup
def demo6():    
    headers = {
            'Host': 'www.toutiao.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
            'Connection': 'Keep-Alive',
            'Content-Type': 'text/plain; Charset=UTF-8',
            'Accept': '*/*',
            'Accept-Language': 'zh-cn',
            'cookie':'__tasessionId=u690hhtp21501983729114;cp=59861769FA4FFE1'}
    url = 'https://www.toutiao.com/a6546106375104102926/'    
    ttp = requests.get(url,headers)
    wbdata = requests.get(url).text
    soup = BeautifulSoup(wbdata,'lxml')
    list = soup.find_all('script')
    
    for index in list:
        print index
        print "------------------------------------------"

def demo7():
    str = '''{userInfo:{id: 0,userName: '',avatarUrl: '',isPgc: false,isOwner: false}}'''
    print str
    json_str = json.loads(""+str)
    
    print json_str
    
#     测试scrapy-splash

from scrapy.selector import Selector
def demo8():    
    headers = {
            'Host': 'www.toutiao.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
            'Connection': 'Keep-Alive',
            'Content-Type': 'text/plain; Charset=UTF-8',
            'Accept': '*/*',
            'Accept-Language': 'zh-cn',
            'cookie':'__tasessionId=u690hhtp21501983729114;cp=59861769FA4FFE1'}
    
    splash_url = 'http://192.168.139.131:8050/render.html'
    args = {'url':'https://www.toutiao.com/c/user/article/?page_type=1&user_id=3672368498&max_behot_time=0&count=20&as=A1B54B913E11F59&cp=5B1E812F55E91E1&_signature=t6g.3xAY7MQdh39fciiJU7eoP8','timeout':10,'image':0}
    response = requests.get(splash_url, params = args)
    
    sel = Selector(response)
    print response.text
    print "\n".join(sel.css('div.quote span.text::text').extract()  )
    
def demo9():    
    splash_url = 'http://192.168.139.129:8050/render.html'
    args = {'url':'https://www.toutiao.com/search/?keyword=刮痧拔罐','timeout':10,'image':0}
    response = requests.get(splash_url,params = args)
    sel = Selector(response)
    print "".join(sel.xpath('//body').extract())
    content_list = sel.xpath('//span[@class="J_title"]')
    count = 1
    for content in content_list:
        arr = content.xpath('.//text()').extract()
        print("{}、{}".format(count,"".join(arr) )) 
        count+=1   
        
if __name__ == '__main__':
    
    demo8()
    print 'end'
    
    
           