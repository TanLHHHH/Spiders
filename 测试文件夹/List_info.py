#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 14:44
# @Author  : TanLHHH
# @Site    : 
# @File    : List_info.py
# @Software: PyCharm
detail_info= ['"zguidh":"1930022396216614993","premieragent":"no","fsbid":"9457","aamgnrc1":"905-LJuniperStNE","hood":"Midtown","city":"Atlanta","state":"GA","zip":"30309","mlat":"33798592","mlong":"-84388297","listtp":"building","proptp":"cnd","sqft":"700,1898,2144,2773","sqftrange":"500-1000,1500-2000,2000-2500,2500-3000","price":"5750,10500,340585,636379,639489,661056","prange":"5000-6000,10000_and_up,300000-350000,600000-700000","bd":"1,3","pid":"2431572814","ba":"1,3,35"']

print(detail_info[0])

dict = eval('{'+detail_info[0]+'}')
print(type(dict))