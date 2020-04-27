#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 17:55
# @Author  : TanLHHH
# @Site    : 
# @File    : 口语文本.py
# @Software: PyCharm

import requests
from lxml import etree


url = "https://top.zhan.com/toefl/speak/feedback-385-13.html"
html = requests.get(url=url).content.decode('utf-8')

selector = etree.HTML(html)
content = selector.xpath('/html/body/div[4]/div[1]/div/div/div/p/text()')
print(content)