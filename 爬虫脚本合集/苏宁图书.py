#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 16:40
# @Author  : TanLHHH
# @Site    : 
# @File    : 苏宁图书.py
# @Software: PyCharm

import re
import requests
import json
import random

# user_agent列表
user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
]


#获取大分类列表
def get_big():
    # 获取一个代理，格式为ip:端口
    headers = {'User-Agent':random.choice(user_agent_list)}
    res = requests.get(url='https://book.suning.com/', timeout=3, headers = headers)
    data = res.content.decode('utf-8')
    str = '<h3><a name=".*?" target="_blank" href="(.*?)">'
    big_url_list = re.compile(str,re.S).findall(data)
    return big_url_list

    



if __name__ == '__main__':
    get_big()