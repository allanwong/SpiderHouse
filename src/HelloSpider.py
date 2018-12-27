#coding=utf-8 
'''
Created on 2018年6月1日

@author: bingqiw
'''
# selenium解析html页面

from selenium import webdriver

import os

def demo():
#   https://www.cnblogs.com/technologylife/p/5829944.html
#   上面安装说明  
    chromedriver="D:\Program Files\eclipse4.6\workspace\SpiderHouse\src\chromedriver.exe"
    os.environ["webdriver.chrome.driver"]=chromedriver
    options = webdriver.ChromeOptions()
    
    #去掉不受支持的命令行标记
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    
    #设置成用户自己的数据目录
    options.add_argument('--user-data-dir=D:/tmp') 
    
    driver=webdriver.Chrome(chromedriver, chrome_options=options)
    try:
        driver.get("http://www.baidu.com")
        print(driver.page_source)
    except BaseException, err: 
        print(err)
    
    
    
#     browser = webdriver.Chrome()
#     browser.get("http://www.baidu.com")
#     print(browser.page_source)
#     browser.close() 
    print("end")
    
if __name__ == '__main__':
    demo()
    
    
    
           