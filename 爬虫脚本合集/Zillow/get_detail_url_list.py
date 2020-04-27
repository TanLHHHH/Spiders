#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 23:17
# @Author  : TanLHHH
# @Site    : 
# @File    : get_detail_url_list.py
# @Software: PyCharm

import requests
import re


class get_detail_url_list():

    def __init__(self):
        self.detail_url_list = []
        self.read_json()
    def read_json(self):
        with open('./json/Apartment.json',"r",encoding='utf-8') as f:
            string = f.readlines()
            pat = '"detailUrl": "(.*?)"'
            list = re.compile(pat,re.S).findall(str(string))
            self.list1 = list
        f.close()

        with open('./json/Apartment-2.json', "r", encoding='utf-8') as f:
            string = f.readlines()
            pat = '"detailUrl": "(.*?)"'
            list = re.compile(pat, re.S).findall(str(string))
            self.list2 = list
        f.close()

        with open('./json/homedetails.json', "r", encoding='utf-8') as f:
            string = f.readlines()
            pat = '"detailUrl": "(.*?)"'
            list = re.compile(pat, re.S).findall(str(string))
            self.list3 = list
        f.close()

    def print_list(self):
        print(self.list1)
        print("""--------""")
        print(self.list2)
        print("""--------""")
        print(self.list3)
        print("-------")
        print("list 总长度为：", len(self.list1) + len(self.list2)+len(self.list3))




