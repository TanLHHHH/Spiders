#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 19:23
# @Author  : TanLHHH
# @Site    : 
# @File    : lianjiajia.py
# @Software: PyCharm

import json
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import re
import csv
import os
#import pandas as pd
#import pymongo

session = requests.session()


def generate_allurl(user_in_nub, user_in_city):  # 生成url
    url = 'http://' + user_in_city + '.lianjia.com/chengjiao/pg{}/'
    for url_next in range(1, int(user_in_nub)):
        #print("当前访问：",url.format(url_next))
        yield url.format(url_next)


def get_allurl(generate_allurl):  # 分析url解析出每一页的详细url
    # 这里模拟一下请求头，头文件是从浏览器里面抓到的，否则服务会回复403错误，（其实就是服务器做的简单防爬虫检测）
    headers = {
        'Host': 'zj.lianjia.com',
        'Referer' :'https://zj.lianjia.com/ershoufang/',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie' : 'TY_SESSION_ID=01d42053-b6d8-41ae-946f-81d11bce4b12; lianjia_uuid=78034c73-5798-4752-846f-4af18cdda8bd; _ga=GA1.2.999189367.1585214204; _gid=GA1.2.387378222.1585214204; UM_distinctid=17116212940fe-072b3a69df46f4-396a7f06-1fa400-171162129417ed; sajssdk_2015_cross_new_user=1; _smt_uid=5e7c739c.38edfb41; lianjia_ssid=3cfc91eb-b325-47fa-b3ac-e6e1758417ed; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1585214366,1585221444; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217116239bc03d9-02366034317f66-396a7f06-2073600-17116239bc1bc2%22%2C%22%24device_id%22%3A%2217116239bc03d9-02366034317f66-396a7f06-2073600-17116239bc1bc2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fblog.csdn.net%2FQwertyuiop2016%2Farticle%2Fdetails%2F84445010%22%2C%22%24latest_referrer_host%22%3A%22blog.csdn.net%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; select_city=321100; CNZZDATA1255633284=305496514-1585212233-%7C1585222157; CNZZDATA1255604082=19241345-1585212590-%7C1585221337; CNZZDATA1254525948=1527300022-1585211921-%7C1585223009; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1585223922; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYmY5ZDQwMGUzZWM2OTM1YzE5NGJlMzgzM2I2ZjdjMDE1ODI5MTU1NmE3MjZjZTI4MjA4OThjY2Q0MDgxYTI1NTNhY2Y0NjEzYzhjYzk0NmIxYmMwZTFkOTg3YzExMWI4OGRlYzEyMjE4MGQ0Y2FmMGNkZjlkMjVhNTM3YmUxZWIzNWM0YzljODdmN2MxMWZjOTQwMzIxNmRhNjUwZTA0MGYxOGJhM2E3N2I0Y2VkMjg1ZWMxOTRiN2IyOTA4OTQ0ZmY2ZDYzYTY2NWY5NDllYjk0M2U4NGJiNzI0ZTM4NDVlYWIzZDU4ODRkZDYwZDJkOTA0ZTFmZWQ3NjFiZDcxZGQwMzFkNmEzOGNmYThkOGUzNDU2MTY4ZGJlOTFkYTVlZTBjOWQyYTU1ODBlMTk5ZTY1MDg0MDZjZTAxZTQwZWFcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiM2UyY2E2ZjRcIn0iLCJyIjoiaHR0cHM6Ly96ai5saWFuamlhLmNvbS9jaGVuZ2ppYW8vIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='

    }
    session.headers.clear()
    session.headers.update(headers)
    get_url = session.get(generate_allurl)
    print("当前url",generate_allurl)
    if get_url.status_code == 200:
        #print(get_url.status_code)
        # 原来代码用没有正则搜索出结果，这里屏蔽下，用BS完成所有赛选
        # re_set = re.compile('<li.*?class="clear">.*?<a.*?class="img.*?".*?href="(.*?)"')
        # re_get = re.findall(re_set, get_url.text)
        soup = BeautifulSoup(get_url.text, 'lxml')
        # liitem = soup.findall('li',{'class':'clear LOGCLICKDATA'})
        urls = []
        #liitems = soup.select('li.clear.LOGCLICKDATA')
        liitems = soup.select('.img')

        #print(len(liitems))

        for item in liitems:
            #print(item)
            pat = 'href="(.*?)"'
            url = re.compile(pat, re.S).findall(str(item))
            urls.append(url[0])
        #print("Urls",urls)
        return urls


def open_url(re_get):  # 分析详细url获取所需信息

    headers = {
        'Host': 'zj.lianjia.com',
        'Connection': 'keep-alive',
        'Referer': 'https://zj.lianjia.com/ershoufang/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie' : 'TY_SESSION_ID=01d42053-b6d8-41ae-946f-81d11bce4b12; lianjia_uuid=78034c73-5798-4752-846f-4af18cdda8bd; _ga=GA1.2.999189367.1585214204; _gid=GA1.2.387378222.1585214204; UM_distinctid=17116212940fe-072b3a69df46f4-396a7f06-1fa400-171162129417ed; sajssdk_2015_cross_new_user=1; _smt_uid=5e7c739c.38edfb41; lianjia_ssid=3cfc91eb-b325-47fa-b3ac-e6e1758417ed; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1585214366,1585221444; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217116239bc03d9-02366034317f66-396a7f06-2073600-17116239bc1bc2%22%2C%22%24device_id%22%3A%2217116239bc03d9-02366034317f66-396a7f06-2073600-17116239bc1bc2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fblog.csdn.net%2FQwertyuiop2016%2Farticle%2Fdetails%2F84445010%22%2C%22%24latest_referrer_host%22%3A%22blog.csdn.net%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; select_city=321100; CNZZDATA1255633284=305496514-1585212233-%7C1585222157; CNZZDATA1255604082=19241345-1585212590-%7C1585221337; CNZZDATA1254525948=1527300022-1585211921-%7C1585223009; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1585223922; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYmY5ZDQwMGUzZWM2OTM1YzE5NGJlMzgzM2I2ZjdjMDE1ODI5MTU1NmE3MjZjZTI4MjA4OThjY2Q0MDgxYTI1NTNhY2Y0NjEzYzhjYzk0NmIxYmMwZTFkOTg3YzExMWI4OGRlYzEyMjE4MGQ0Y2FmMGNkZjlkMjVhNTM3YmUxZWIzNWM0YzljODdmN2MxMWZjOTQwMzIxNmRhNjUwZTA0MGYxOGJhM2E3N2I0Y2VkMjg1ZWMxOTRiN2IyOTA4OTQ0ZmY2ZDYzYTY2NWY5NDllYjk0M2U4NGJiNzI0ZTM4NDVlYWIzZDU4ODRkZDYwZDJkOTA0ZTFmZWQ3NjFiZDcxZGQwMzFkNmEzOGNmYThkOGUzNDU2MTY4ZGJlOTFkYTVlZTBjOWQyYTU1ODBlMTk5ZTY1MDg0MDZjZTAxZTQwZWFcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiM2UyY2E2ZjRcIn0iLCJyIjoiaHR0cHM6Ly96ai5saWFuamlhLmNvbS9jaGVuZ2ppYW8vIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='
    }
    session.headers.clear()
    session.headers.update(headers)

    res = session.get(re_get)
    if res.status_code == 200:
        info = {}
        soup = BeautifulSoup(res.text, 'lxml')
        info['标题'] = soup.select('.wrapper')[0].text
        info['总价'] = soup.select('.dealTotalPrice')[0].text
        info['挂牌价'] = soup.select('body > section.wrapper > div.overview > div.info.fr > div.msg > span:nth-child(1) > label')[0].text + '万'
        info['每平方售价'] = soup.select('body > section.wrapper > div.overview > div.info.fr > div.price > b')[0].text + '元'
        info['成交日期'] = soup.select('body > div.house-title > div > span')[0].text

        #info['建造时间'] = soup.select('.subInfo')[2].text
        info['装修情况'] = soup.select('#introduction > div.introContent > div.base > div.content > ul > li:nth-child(9)')[0].text
        info['楼层情况'] = soup.select('#introduction > div.introContent > div.base > div.content > ul > li:nth-child(2)')[0].text
        info['链家编号'] = soup.select('#introduction > div.introContent > div.transaction > div.content > ul > li:nth-child(1)')[0].text

        # info['小区名称'] = soup.select('.info')[0].text
        # info['所在区域'] = soup.select('.info a')[0].text + ':' + soup.select('.info a')[1].text
        # info['链家编号'] = str(re_get)[34:].rsplit('.html')[0]

        # for i in soup.select('.base li'):
        #     i = str(i)
        #     if '</span>' in i or len(i) > 0:
        #         key, value = (i.split('</span>'))
        #         info[key[24:]] = value.rsplit('</li>')[0]
        # for i in soup.select('.transaction li'):
        #     i = str(i)
        #     if '</span>' in i and len(i) > 0 and '抵押信息' not in i:
        #         key, value = (i.split('</span>'))
        #         info[key[24:]] = value.rsplit('</li>')[0]
        print(info)
        return info


# def update_to_MongoDB(one_page):  # update储存到MongoDB
#     Mongo_Url = 'localhost'
#     Mongo_DB = 'Lianjia'
#     Mongo_TABLE = 'Lianjia' + '\n' + str('zs')
#     client = pymongo.MongoClient(Mongo_Url)
#     db = client[Mongo_DB]
#     if db[Mongo_TABLE].update({'链家编号': one_page['链家编号']}, {'$set': one_page}, True):  # 去重复
#         # print('储存MongoDB 成功!')
#         return True
#     return False

#
# # pandas写excel只找到了一次写入没找到追加方式，暂时不用吧
# def pandas_to_xlsx(info):  # 储存到xlsx
# #     pd_look = pd.DataFrame(info, index=False)
# #     pd_look.to_excel('链家二手房.xlsx', sheet_name='链家二手房')
#     print(info)


def writer_to_csv(list):  # 储存到csv


        # writer.writerow({'Address': home_info['Address'],
        #                  'price': home_info['price'],
        #                  'sqft': home_info['sqft'],
        #                  'bd': home_info['bd'],
        #                  'ba': home_info['ba']})
        # csv_file.close()
        #


    fieldnames = ["标题","总价","挂牌价","每平方售价","成交日期","装修情况","楼层情况","链家编号"]
    with open('链家镇江成交房.csv', 'a', encoding='utf-8',newline='')as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        if os.path.getsize("链家镇江成交房.csv") == 0:
            writer.writeheader()
        writer.writerow(list)
        f.close()


def main(url):
    info = open_url(url)
    writer_to_csv(info)  # 储存到text文件
    # pandas_to_xlsx(info)    #储存到xlsx文件
    # update_to_MongoDB(info)  # 储存到Mongodb


if __name__ == '__main__':
    # user_in_city = input('输入爬取城市：')
    # user_in_nub = input('输入爬取页数：')

    pool = Pool()
    for i in generate_allurl('35', 'zj'):
        pool.map(main, [url for url in get_allurl(i)])