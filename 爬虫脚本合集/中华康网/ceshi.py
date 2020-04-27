#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 12:42
# @Author  : TanLHHH
# @Site    : 
# @File    : ceshi.py
# @Software: PyCharm
import requests
import re

url = 'http://www.cnkang.com/yyk/hospdept/2062/'

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
           'Accept':':text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.9'}

res = requests.get(url,headers = headers)

name_pat = '<div class="ys11_name"><ul class="left">(.*?)</ul> <p><span></span><em></em>(.*?)</p></div>'
name = re.compile(name_pat,re.S).findall(res.content.decode('utf-8'))
print(name)

big_class_pat = '<a href="javascript:;" class="link06">(.*?)</a>'
big_class = re.compile(big_class_pat,re.S).findall(res.content.decode('utf-8'))
print(big_class)

#print(res.content.decode('utf-8'))

little_class_pat = '<ol><a href="javascript:;" class="link06">妇儿</a></ol>.*?<li><a href="(.*?)">(.*?)</a><em>.*?</em></li>.*?</ul>'
listtle_class = re.compile(little_class_pat,re.S).findall(res.content.decode('utf-8'))
print(listtle_class)