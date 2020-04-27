#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 11:54
# @Author  : TanLHHH
# @Site    : 
# @File    : zillow_session.py
# @Software: PyCharm

import requests

s = requests.Session()

res=s.get(url="https://www.zillow.com/")

print(res.text)