#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 16:38
# @Author  : TanLHHH
# @Site    : 
# @File    : 百度贴吧.py
# @Software: PyCharm

import requests
import random
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

def get_proxy():
    return requests.get("http://192.144.162.135:5010/get/").json()
def delete_proxy(proxy):
    requests.get("http://192.144.162.135:5010/delete/?proxy={}".format(proxy))

#得到列表页html
def get_html():
    proxy = get_proxy().get("proxy")
    for i in range(0,631):
        print("当前正在爬取第",i,"页")
        headers={
            'User-Agent':random.choice(user_agent_list),
            'Host': 'tieba.baidu.com',
            'Connection': 'keep-alive'
        }
    try:
        cur_url = 'https://tieba.baidu.com/f?kw=%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92&ie=utf-8&pn={}'.format(i*50)
        res = requests.get(url=cur_url,headers=headers,proxies={"http": "http://{}".format(proxy)})
        # 使用代理访问
        parsing_list_html(res.content.decode('utf-8'))
    except Exception as e:
        print(e)


#解析列表页
def parsing_list_html(content):
    #详情页URL代号
    detail_number_pat = '<a rel="noreferrer" href="/p/(.*?)"'
    detail_number_list = re.compile(detail_number_pat,re.S).findall(content)
    print(detail_number_list)

    #标题列表
    title_pat = '<a rel="noreferrer" href="/p/.*?" title="(.*?)"'
    title_list = re.compile(title_pat,re.S).findall(content)
    print(title_list)

    #发帖人名称列表
    postman_pat = 'title="主题作者:(.*?)"'
    postman_list = re.compile(postman_pat,re.S).findall(content)
    print(postman_list)

    #发帖人主页
    #postman_url_pat = 'class="frs-author-name j_user_card " href="(.*?)" target="_blank">'
    postman_url_pat = 'title="主题作者:.*?".*? href="/home/main/(.*?)&fr=frs" target="_blank">'
    postman_url_list = re.compile(postman_url_pat,re.S).findall(content)
    #print("发帖人数量为：",len(postman_url_list))

    #发帖时间
    post_time_pat = '<span class="pull-right is_show_create_time" title="创建时间">(.*?)</span>'
    post_time_list = re.compile(post_time_pat,re.S).findall(content)
    print(post_time_list)


    #主页内容
    content_list=get_content(detail_number_list)
    print("主页内容：",content_list)


    with open("tiezi_info.csv","a",encoding="utf-8",newline='') as csv_file:
        writer = csv.writer(csv_file)
        if os.path.getsize("tiezi_info.csv") == 0:
            writer.writerow(('标题','发帖人','发帖时间','帖子内容'))
        rows = zip(title_list,postman_list,post_time_list,content_list)
        for row in rows:
            writer.writerow(row)
        csv_file.close()

    get_postman_info(postman_url_list)


def get_content(detail_number_list):
    content_list = []
    for i in range(0,len(detail_number_list)):
        try:
            proxy = get_proxy().get("proxy")
            cur_url = "https://tieba.baidu.com/p/"+str(detail_number_list[i])
            headers = {
                'User-Agent': random.choice(user_agent_list),
                'Host': 'tieba.baidu.com',
                'Connection': 'keep-alive'
            }
            res = requests.get(url=cur_url,proxies={"http": "http://{}".format(proxy)},headers=headers)
            pat = '<div id="post_content_.*?" class="d_post_content j_d_post_content  clearfix" style="display:;">            (.*?)</div><br>'
            content = re.compile(pat, re.S).search(res.content.decode('utf-8'))
            print("当前主页为：",cur_url)
            #print("当前主页内容为",content.groups())
            #print(type(content.groups()))
            content_list.append(str(content.groups()))
        except Exception as e:
            print(e)
    return content_list

from bs4 import BeautifulSoup
def get_soup(url):
    try:
        proxy = get_proxy().get("proxy")
        headers = {
            'User-Agent': random.choice(user_agent_list),
            'Host': 'tieba.baidu.com',
            'Connection': 'keep-alive'
        }

        wb_data = requests.get(url,headers=headers,proxies={"http": "http://{}".format(proxy)})
        soup = str(BeautifulSoup(wb_data.text,'lxml'))
    except Exception as e:
        print(e)
    return soup

def get_postman_info(postman_list):
    for i in range(0,len(postman_list)):
        cur_url = 'https://tieba.baidu.com/' +'/home/main/' +str(postman_list[i])
        print("当前用户url为：",cur_url)
        new_soup = get_soup(cur_url)

        # 用户名称
        user_name = re.compile('<span class="userinfo_username.*?">(.*?)<', re.S)
        name = re.findall(user_name, new_soup)
        print("用户名称",name)

        # 获取性别
        user_sexs = re.compile(r'<span class="userinfo_sex userinfo_sex_(.*?)">', re.S)
        sexs = re.findall(user_sexs, new_soup)
        print("用户性别",sexs)

        # 获取吧龄
        tieba_ages = re.compile(r'<span>吧龄:(.*?)</span>', re.S)
        ages = re.findall(tieba_ages, new_soup)
        print("用户年龄",ages)

        # 获取发帖数
        tieba_notes = re.compile(r'<span>发贴:(.*?)</span>', re.S)
        notes = re.findall(tieba_notes, new_soup)
        print("发帖数",notes)

        # 获取礼物数
        tieba_gifts = re.compile(r'<i>(.*?)</i>', re.S)
        gifts = re.findall(tieba_gifts, new_soup)
        print("礼物数",gifts)

        # 获取关注数
        user_favorites = re.compile(r'<a href="/home/concern(.*?)</a>', re.S)
        favorites = re.findall(user_favorites, new_soup)
        if len(favorites) == 1:
            favorite = favorites[0].split(r'>')[-1]
            print('关注数',favorite)
        elif len(favorites) == 0:
            favorite = '0'
            # print(favorite)

        # 获取粉丝数
        user_fans = re.compile(r'<a href="/home/fans(.*?)</a>', re.S)
        fans_num = re.findall(user_fans, new_soup)
        if len(fans_num) == 1:
            fans = fans_num[0].split(r'>')[-1]
            print("粉丝数",fans)
        elif len(fans_num) == 0:
            fans = '0'
            # print(fans)

        with open("postman_info.csv", "a", encoding="utf-8", newline='') as csv_file:
            writer = csv.writer(csv_file)
            if os.path.getsize("postman_info.csv") == 0:
                writer.writerow(['昵称', '性别', '年龄', '发帖数', '礼物数', '粉丝数'])
            rows = zip(name, sexs, ages, notes, gifts, fans)
            for row in rows:
                writer.writerow(row)
            csv_file.close()

def main():
    get_html()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)