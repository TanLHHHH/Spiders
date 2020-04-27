#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 16:43
# @Author  : TanLHHH
# @Site    : 
# @File    : tieba.py
# @Software: PyCharm

import requests,re

url = "https://tieba.baidu.com/f?kw=%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92&ie=utf-8&pn=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Host": "tieba.baidu.com"
}

res = requests.get(url=url,headers=headers)
#print(res.content.decode('utf-8'))

pat = '<a rel="noreferrer" href="/p/(.*?)" title="(.*?)" target="_blank" class="j_th_tit ">'
title_list = re.compile(pat, re.S).findall(res.content.decode('utf-8'))

#url_pat = 'class="frs-author-name j_user_card " href="(.*?)" target="_blank">'



pat = 'title="主题作者:.*?".*? href="/home/main/(.*?)" target="'

url_list = re.compile(pat,re.S).findall(res.content.decode('utf-8'))
print(res.content.decode('utf-8'))
# print(res.status_code)
# print(title_list)
# print(title_list[0][0],title_list[0][1])
print(url_list)
print(len(url_list))