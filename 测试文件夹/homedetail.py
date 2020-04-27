#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 12:26
# @Author  : TanLHHH
# @Site    : 
# @File    : homedetail.py.py
# @Software: PyCharm

import requests
import re


detail_url = "https://www.zillow.com" + '/homedetails/1120-Snyder-St-NW-Atlanta-GA-30318/35909140_zpid/'
print("当前detailURL为：",detail_url)
headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
res = requests.get(url=detail_url,timeout=5,headers=headers)
content = res.content.decode("utf-8")
print(content)

#获取地址
add_pat = '\\\\"streetAddressOnly\\\\":\\\\"(.*?)\\\\"'
streetAddressOnly = re.compile(add_pat,re.S).findall(content)

price_pat = '\\\\"priceForHDP\\\\":(.*?),'
priceForHDP = re.compile(price_pat,re.S).findall(content)

livingArea_pat = '\\\\"livingArea\\\\":(.*?),'
livingArea = re.compile(livingArea_pat,re.S).findall(content)

bedrooms_pat = '\\\\"bedrooms\\\\":(.*?),'
bedrooms = re.compile(bedrooms_pat,re.S).findall(content)

bathroom_pat = '\\\\"bathrooms\\\\":(.*?),'
bathroom = re.compile(bathroom_pat,re.S).findall(content)

print(streetAddressOnly,priceForHDP,livingArea,bedrooms,bathroom)