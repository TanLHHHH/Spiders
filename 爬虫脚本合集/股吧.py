#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 20:29
# @Author  : TanLHHH
# @Site    : 
# @File    : 股吧.py
# @Software: PyCharm
# 需要数据：标题、阅读量、评论、发帖时间需加上年份


import requests
import random
import time
import re
import csv
import os
# user_agent列表
user_agent_list=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
]
headers = {
    'User-Agent':random.choice(user_agent_list),
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'st_pvi=87732908203428;st_si=12536249509085;qgqp_b_id=9777e9c5e51986508024bda7f12e6544;_adsame_fullscreen_16884=1',
    'Host':'guba.eastmoney.com',
    'Referer':'http://guba.eastmoney.com/list,600596,f_1.html',
    'Upgrade-Insecure-Requests':'1',
    }
#构建IP代理池
def get_proxy():
    return requests.get("http://192.144.162.135:5010/get/").json()
def delete_proxy(proxy):
    requests.get("http://192.144.162.135:5010/delete/?proxy={}".format(proxy))



def get_detail_url():
    """
    获取当前页面详情页URL
    :return: detail_url_list
    """
    url = 'https://guba.eastmoney.com/list,zssh000001,99_{}.html'

    #爬去列表页 从中获得详情页 URL
    for i in range(1,100):
        print("-----------------当前正在爬去第",i,"页--------------------------")
        print("当前列表页的URL为",url.format(i))
        proxy = get_proxy().get("proxy")
        res = requests.get(url=url.format(i),headers=headers,proxies={"http": "http://{}".format(proxy)})
        print(res.status_code)
        detail_url_list_pat = '<span class="l3 a3"><a href="(.*?)"'
        detail_url_list = re.compile(detail_url_list_pat,re.S).findall(res.content.decode('utf-8'))
        get_detail_info(detail_url_list)
        #time.sleep(5)

def get_detail_info(detail_url_list):
    """
    解析详情页 获取标题 阅读量 评论 发帖时间（需加上年份）
    :param detail_url_list:
    :return:
    """
    url='https://guba.eastmoney.com'
    for i in range(0,len(detail_url_list)):
        #信息字典
        info = {}
        cur_url = url + detail_url_list[i]
        print("当前详情页为：",cur_url)
        proxy = get_proxy().get("proxy")
        res = requests.get(cur_url,headers=headers,proxies={"http": "http://{}".format(proxy)})
        print("proxy:",proxy)
        #标题
        title_pat = '<div id="zwconttbt">(.*?)</div>'
        title = re.compile(title_pat,re.S).findall(res.content.decode('utf-8'))
        title[0] = title[0].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
        info['title'] = title[0]
        print(title)
        #阅读量
        read_num_pat= '"post_click_count":(.*?),'
        read_num = re.compile(read_num_pat,re.S).findall(res.content.decode('utf-8'))
        info['read_num'] = read_num[0]
        print(read_num)
        #发表时间
        post_time_pat='<div class="zwfbtime">(.*?)</div>'
        post_time = re.compile(post_time_pat,re.S).findall(res.content.decode('utf-8'))
        info['post_time'] = post_time[0]
        print("发表时间为",post_time)

        #评论
        comments_pat = '<div class="short_text">(.*?)</div>'
        comments = re.compile(comments_pat,re.S).findall(res.content.decode('utf-8'))
        if comments:
            for x in range(0,len(comments)):
                comments[x] = comments[x].replace('\r','').replace('\n','').replace('\t','').replace(' ','')
        info['comments'] = comments
        write_to_csv(info)
        #time.sleep(5)


def write_to_csv(info):
    fieldnames = ["标题","阅读量","发帖时间","评论"]
    with open('guba_info.csv','a',encoding='utf-8_sig',newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if os.path.getsize("guba_info.csv") == 0:
            writer.writeheader()
        writer.writerow({'标题':info['title'],
                         '阅读量':info['read_num'],
                         '发帖时间':info['post_time'],
                         '评论':info['comments']})
        csv_file.close()
        print("以保存")

if __name__ == '__main__':
    get_detail_url()