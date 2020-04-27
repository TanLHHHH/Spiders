#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 00:27
# @Author  : TanLHHH
# @Site    :
# @File    : 携程_详情页_url.py
# @Software: PyCharm

# *^-^* coding:utf-8 *^-^*

import requests
import re
url = 'https://vacations.ctrip.com/list/around/d-hubei-100067.html?filter=n1&p=1'
res = requests.get(url)
print(res.status_code)
#print(res.content.decode('utf-8'))

pat = '"products":(.*?),"crumbs":'
products_info = re.compile(pat,re.S).findall(res.content.decode('utf-8'))
detail_url_pat = '"detailUrl":"(.*?)",'
detail_url_list = re.compile(detail_url_pat,re.S).findall(products_info[0])

products_id_pat = '"id":(.*?),'
products_id_list = re.compile(products_id_pat,re.S).findall(products_info[0])

#print(products_info[0])

print(products_id_list)

# print(detail_url_list)
# print(len(detail_url_list))