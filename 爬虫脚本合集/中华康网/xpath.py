#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 13:14
# @Author  : TanLHHH
# @Site    : 
# @File    : xpath.py
# @Software: PyCharm

import requests
import lxml
from lxml import etree

url = 'http://www.cnkang.com/yyk/hospdept/2062/'

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
           'Accept':':text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.9'}

res = requests.get(url,headers = headers)
#print(res.content.decode('utf-8'))
mytree = lxml.etree.HTML(res.content.decode('utf-8'))
print(mytree)
#print(mytree.xpath("//ol/a[@class='link06']/text()"))
#print(mytree.xpath("//a[@class='link06']/../..//li/a/@href"))
#print(mytree.xpath("//a[@class='link06']/../..//li/a/text()"))
print(mytree.xpath('//div[@class="ys11_name"]/ul/text()'))

divs = mytree.xpath('//div[@class="yslist06 yslist06b"]/div')
for div in divs:
    big_class_name = div.xpath('./ol/a/text()')
    print(big_class_name)
    little_class_list = div.xpath('./ul/li')
    for li in little_class_list:
        print(li.xpath("./a/@href"))
        print(li.xpath("./a/text()"))