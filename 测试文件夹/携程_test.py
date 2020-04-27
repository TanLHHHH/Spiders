#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 21:32
# @Author  : TanLHHH
# @Site    : 
# @File    : 携程_test.py
# @Software: PyCharm
# *^-^* coding:utf-8 *^-^*

import requests
import json

url = 'https://vacations.ctrip.com/tour/restapi/online/12447/ProductDetailTimingV5?_fxpcqlniredt=09031174410487229982'

data = {"ChannelCode":0,
        "PlatformId":4,
        "Version":"80400",
        "Locale":"zh-CN",
        "head":{"cid":"09031174410487229982","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":"","extension":[]},
        "ProductId":18205233,
        "DepartureCityId":477,
        "QueryNode":{"IsTravelIntroductionInfo":
                         "true","IsBookInfo":"true",
                     "IsBasicExtendInfo":"true","IsSegmentInfo":"true"},"contentType":"json"}
Header = {
    'Content-Type': 'application/json',
}


res = requests.post(url,data=json.dumps(data),headers=Header)
print(res.content.decode('utf-8'))