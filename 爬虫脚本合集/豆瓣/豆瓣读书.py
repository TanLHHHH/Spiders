#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 23:39
# @Author  : TanLHHH
# @Site    : 
# @File    : 豆瓣读书.py
# @Software: PyCharm

import requests
import lxml
from lxml import etree

url = "https://book.douban.com/subject/25862578/comments/hot?p=5"

res = requests.get(url)

mytree = lxml.etree.HTML(res.content.decode('utf-8'))

short_list = mytree.xpath("//span[@class='short']/text()")

print(short_list)