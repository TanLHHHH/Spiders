#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 00:15
# @Author  : TanLHHH
# @Site    : 
# @File    : 携程测试.py
# @Software: PyCharm

URL = 'https://jobs.51job.com/guangzhou-thq/121053789.html?s=01&t=0'
import requests
import re

res = requests.get(URL)
print(res.status_code)
print(res.content.decode('gbk'))
pat = '<p class="fp"><span class="label">职能类别：</span><a class="el tdn" href=".*?">(.*?)</a><a class="el tdn" href=".*?">(.*?)</a></p>'
leibie = re.compile(pat,re.S).findall(res.content.decode('gbk'))
print(leibie)

#pat1 = '<div class="com_tag"><p class="at" title=".*?"><span class="i_flag"></span>.*?</p><p class="at" title=".*?"><span class="i_people"></span>.*?</p><p class="at" title="(.*?)">'
#fenlei = re.compile(pat1,re.S).findall(res.content.decode('gbk'))
#print(fenlei)

#price_pat = '<dfn>¥</dfn><em>(.*?)</em>'
#price = re.compile(price_pat,re.S).findall(res.content.decode('utf-8'))
#print(price[0])