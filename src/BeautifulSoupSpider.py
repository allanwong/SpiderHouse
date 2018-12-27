#coding=utf-8 
'''
Created on 2018年6月1日

@author: bingqiw
'''
# BeautifulSoup解析html页面
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

def demo():
    soup = BeautifulSoup(html,'lxml')
    print(soup.prettify())
    print("----------------------------------")
    print(soup.title)
    print("----------------------------------")
    print(soup.title.name)
    print("----------------------------------")
    print(soup.title.string)
    print("----------------------------------")
    print(soup.title.parent.name)
    print("----------------------------------")
    print(soup.p)
    print("----------------------------------")
    print(soup.p["class"])
    print("----------------------------------")
    print(soup.a)
    print("----------------------------------")
    print(soup.find_all('a'))
    print("----------------------------------")
    print(soup.find(id='link3'))
    print("----------------------------------")
    print("end")
    
if __name__ == '__main__':
    
    demo()
    
    
    
           