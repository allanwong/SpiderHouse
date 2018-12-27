#coding=utf-8 
'''
Created on 2018年6月1日

@author: bingqiw
'''
# python正则表达式
# re.match()
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None
# 语法格式：
# re.match(pattern,string,flags=0)
import re

def demo():
    content= "hello 123 4567 World_This is a regex Demo"
    result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
    print(result)
    print(result.group())
    print(result.span())
    
if __name__ == '__main__':
    
    demo()
    
    
    
           