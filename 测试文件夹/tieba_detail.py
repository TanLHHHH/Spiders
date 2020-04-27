#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 17:14
# @Author  : TanLHHH
# @Site    : 
# @File    : tieba_detail.py
# @Software: PyCharm


import requests
import re


url = "https://tieba.baidu.com/p/"+"6569679417"

res = requests.get(url=url)
pat = '<div id="post_content_.*?" class="d_post_content j_d_post_content  clearfix" style="display:;">            (.*?)</div><br>'

content = re.compile(pat,re.S).search(res.content.decode('utf-8'))
print(content)
print(content.groups())
print(res.status_code)
#print(res.content.decode('utf-8'))
