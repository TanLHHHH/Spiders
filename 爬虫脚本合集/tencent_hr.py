#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 14:49
# @Author  : TanLHHH
# @Site    : 
# @File    : tencent_hr.py
# @Software: PyCharm

import requests
import lxml
from lxml import etree

header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

}
URL = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1583652994473&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"

res = requests.get(url=URL,headers=header)
data = res.json()
print(data["Data"]["Posts"])

