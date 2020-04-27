#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 18:19
# @Author  : TanLHHH
# @Site    : 
# @File    : 读取csv文件.py
# @Software: PyCharm

import csv
import re


csv_reader = csv.reader(open('data.kb_meituan_waimai_2.csv', encoding='utf-8'))

csv_writer = csv.writer(open('昌宁人民医院_美图外卖.csv', 'a', encoding='utf-8_sig', newline=''))
csv_writer.writerow(['商铺名称','营业时间','地址','月销售量','人均','活动信息'])

for row in csv_reader:
    #print(row)

    name_pat = r"(\d{1,2}:\d{1,2}-\d{1,2}:\d{1,2})\\t(.*?)\\t.*?]"
    name = re.compile(name_pat,re.S).findall(str(row))
    print(name)
    #print("营业时间",name[0])
    #print("店铺名称",name[1])

    address_pat = r"[[]'(.*?)\\t"
    address = re.compile(address_pat,re.S).findall(str(row))
    print(address)

    month_sale_pat = r'月售(.*?)\\t'
    month_sale = re.compile(month_sale_pat,re.S).findall(str(row))
    print("月销售量：",month_sale)

    people_ave_pat = r'人均 ¥(.*?)\\t'
    people_ave = re.compile(people_ave_pat,re.S).findall(str(row))
    print("人均：",people_ave)

    info_pat = r'""info"" : ""(.*?)""'
    info = re.compile(info_pat,re.S).findall(str(row))
    print("info:",info)

    if address[0] == '\\ufeffaddress' :
        pass
    else:
        csv_writer.writerow([name[0][1],name[0][0],address[0],month_sale[0],people_ave,info])
    print("----------------")



