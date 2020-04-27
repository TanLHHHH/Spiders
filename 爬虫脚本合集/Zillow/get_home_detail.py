#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 23:50
# @Author  : TanLHHH
# @Site    : 
# @File    : get_home_detail.py
# @Software: PyCharm

import requests
from requests.exceptions import SSLError

from Zillow.get_detail_url_list import get_detail_url_list
import re
import csv
import os
import random

# user_agent列表
user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",

                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
]




class get_home_detail():


    def __init__(self):
        self.detail_url_list = get_detail_url_list()
        self.list_url = []
        self.list_url.append(self.detail_url_list.list1)
        self.list_url.append(self.detail_url_list.list2)
        self.list_url.append(self.detail_url_list.list3)


        self.detail_url_list.print_list()

    def detail_url_requests_1(self):
        for x in range(0,len(self.list_url)):
            for i in range(0,len(self.list_url[x])):
                try:
                    detail_url = "https://www.zillow.com" + self.list_url[x][i]
                    print("当前detailURL为：",detail_url)
                    headers = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                            'accept-encoding': 'gzip, deflate, sdch, br',
                            'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
                            'cache-control': 'max-age=0',
                            'upgrade-insecure-requests': '1',
                            'user-agent': random.choice(user_agent_list)
                        }
                    res = requests.get(url=detail_url,timeout=2,headers=headers)
                    content = res.content.decode("utf-8")

                    #判断 /b 为公寓类型
                    if self.list_url[x][i][1] == 'b':
                        #获取地址
                        pat = '"fullAddress":"(.*?)"'
                        Address = re.compile(pat,re.S).findall(content)
                        #print("当前List1",i,"确切地址为：",Address)
                        #获取具体信息字典
                        info_pat = '"adTargets":{(.*?)},'
                        info = re.compile(info_pat,re.S).findall(content)
                        if info:
                            #print(info[0])
                            dict_info = eval('{'+info[0]+'}')
                            #print(type(dict_info))
                            #print("当前List1",i,"信息字典为：",dict_info)
                            #写入数据
                            self.write_to_csv_apartment(dict_info,Address)
                        else:
                            print("info值为空")
                    # /homedetails 为整套房屋
                    else:
                        house_dict = {}
                        # 获取地址
                        add_pat = '\\\\"streetAddressOnly\\\\":\\\\"(.*?)\\\\"'
                        streetAddressOnly = re.compile(add_pat, re.S).findall(content)
                        house_dict['Address'] = streetAddressOnly

                        price_pat = '\\\\"priceForHDP\\\\":(.*?),'
                        priceForHDP = re.compile(price_pat, re.S).findall(content)
                        house_dict['Price'] = priceForHDP

                        livingArea_pat = '\\\\"livingArea\\\\":(.*?),'
                        livingArea = re.compile(livingArea_pat, re.S).findall(content)
                        house_dict['livingArea'] = livingArea

                        bedrooms_pat = '\\\\"bedrooms\\\\":(.*?),'
                        bedrooms = re.compile(bedrooms_pat, re.S).findall(content)
                        house_dict['bedrooms'] = bedrooms

                        bathroom_pat = '\\\\"bathrooms\\\\":(.*?),'
                        bathroom = re.compile(bathroom_pat, re.S).findall(content)
                        house_dict['bathroom'] = bathroom

                        #写入数据
                        self.write_to_csv_homedetail(house_dict)


                except requests.exceptions.ConnectionError as e:
                    print("当前list 第",i,"发生异常",e)
                except requests.exceptions.ReadTimeout as e:
                    print("当前list 第",i,"发生异常",e)
                else:
                    pass
    # @classmethod
    # def write_to_csv(self,home_info,Address):
    #     with open("Zillow_1400_home_info.csv","a",encoding="utf-8",newline='') as csv_file:
    #         if os.path.getsize(csv_file):
    #             self.filednames = ["Address","price","sqft","bd","ba"]
    #             csv_writer = csv.DictWriter(csv_file,filednames=self.filednames)
    #             #根据表头写入数据
    #             print("待写入的数据：",Address[0],home_info['price'],home_info['sqft'],home_info['bd'],home_info['ba'])
    #
    #             csv_writer.writerow({'Address':Address[0],
    #                                  'price':home_info['price'],
    #                                  'sqft':home_info['sqft'],
    #                                  'bd':home_info['bd'],
    #                                  'ba':home_info['ba']})
    #             csv_file.close()
    #         else:
    #             csv_writer = csv.writer(csv_file)
    #             csv_writer.writerow(["Address","price","sqft","bd","ba"])
    #             csv_file.close()

    # def write_to_csv(self,home_info,Address):
    #     home_info['Address'] = Address[0]
    #     with open("Zillow_1400_home_info.csv","a",newline='',encoding="utf-8") as csv_file:
    #         writer = csv.writer(csv_file)
    #         for key in home_info:
    #             writer.writerow([key,home_info[key]])
    #     csv_file.close()

    def write_to_csv_homedetail(self,house_dict):
        fieldnames = ["Address", "Price", "livingArea", "bedrooms", "bathroom"]
        with open("House_info.csv", "a", encoding="utf-8", newline='') as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
            if os.path.getsize("House_info.csv") == 0:
                writer.writeheader()
            #writer.writerow([house_list[0],house_list[1],house_list[2],house_list[3],house_list[4]])
            writer.writerow({'Address': house_dict['Address'],
                             'Price': house_dict['Price'],
                             'livingArea': house_dict['livingArea'],
                             'bedrooms': house_dict['bedrooms'],
                             'bathroom': house_dict['bathroom']})
        csv_file.close()




    def write_to_csv_apartment(self,home_info,Address):
        home_info['Address'] = Address[0]
        fieldnames = ["Address","price","sqft","bd","ba"]
        with open("Apartment_info.csv","a",encoding="utf-8",newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if os.path.getsize("Apartment_info.csv") == 0:
                writer.writeheader()
            writer.writerow({'Address':home_info['Address'],
                            'price':home_info['price'],
                            'sqft':home_info['sqft'],
                            'bd':home_info['bd'],
                            'ba':home_info['ba']})
            csv_file.close()

if __name__ == '__main__':
    try:
        zillow = get_home_detail()
        zillow.detail_url_requests_1()
    except Exception as e:
        print(e)
