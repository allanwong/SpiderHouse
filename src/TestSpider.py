#coding=utf-8
#今日头条
from lxml import etree
import requests
import urllib2,urllib

def get_url():
    url = 'https://www.toutiao.com/ch/news_hot/'
    global count
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
        print response.status_code
        html = response.content
        print html
        tree = etree.HTML(html)
        title = tree.xpath('//a[@class="link title"]/text()')
        source = tree.xpath('//a[@class="lbtn source"]/text()')
        comment = tree.xpath('//a[@class="lbtn comment"]/text()')
        stime = tree.xpath('//span[@class="lbtn"]/text()')
        print len(title)   #0
        print type(title)  #<type 'list'>
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

import time
import utils.DateUtils as du
import re
import hashlib 

def get_as_cp():
    zz ={}
    now = round(time.time())
    print now  #获取计算机时间
    e = hex(int(now)).upper()[2:]  #hex()转换一个整数对象为十六进制的字符串表示
    print e 
    i = hashlib.md5(str(int(now))).hexdigest().upper() #hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    if len(e)!=8:
        zz = {'as': "479BB4B7254C150",
            'cp': "7E0AC8874BB0985"}
        return zz
    n=i[:5]
    a=i[-5:]
    r = ""
    s = ""
    for i in range(5):
        s = s+n[i]+e[i]
    for j in range(5):
        r = r+e[j+3]+a[j]
    zz = {
            'as': "A1" + s + e[-3:],
            'cp': e[0:3] + r + "E1"
        } 
    print zz


def test():
    
    url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=56910045575&max_behot_time=0&count=20&as=A1850B9204AF512&cp=5B24EFD5E1A23E1&_signature=ZB6-TBAbPz7OMf7Mfe.6-mQevl'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'UM_distinctid=163ce6850b6f-04618d2153915d-5e4b2519-100200-163ce6850b77d0; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=d2611e09bc7d0ab14b8b3219c2ca7cb4; uuid="w:a8eb0b6b01e2437fbba625498a7e370b"; login_flag=28690aa057ad3f69da5efd8f3626f0c4; sessionid=bd9815695522ad104b112008a9fb9ae9; uid_tt=4157854dfddcd0a2955a7e7e71198977; sid_tt=bd9815695522ad104b112008a9fb9ae9; sid_guard="bd9815695522ad104b112008a9fb9ae9|1528795280|15552000|Sun\054 09-Dec-2018 09:21:20 GMT"; tt_webid=75382423680; tt_webid=75382423680; cp=5B23756DFC06DE1; __tasessionId=t35z51g0h1529146916397; sso_login_status=0; CNZZDATA1259612802=830401929-1528785696-https%253A%252F%252Fwww.toutiao.com%252F%7C1529147596; utm_source=toutiao',
        'pragma': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    }
    
    response = requests.get(url,headers = headers)
        
    print response.text
    
if __name__ == '__main__':
    count = 0
    get_as_cp()