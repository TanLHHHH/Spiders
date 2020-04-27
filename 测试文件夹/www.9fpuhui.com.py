#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 17:32
# @Author  : TanLHHH
# @Site    : 
# @File    : www.9fpuhui.com.py
# @Software: PyCharm

#下限11 上限 5183
url = 'https://api.9fpuhui.com/puhuiApp/api/selectionProductDetail.html?id=5183'
import requests

res = requests.get(url)
print(res.status_code)
print(res.content.decode('utf-8'))