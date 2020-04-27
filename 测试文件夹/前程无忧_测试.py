#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 22:32
# @Author  : TanLHHH
# @Site    : 
# @File    : 前程无忧_测试.py
# @Software: PyCharm

import requests
from lxml import etree
import csv
import time
import random
import re


fp = open('51job.csv', 'wt', newline='', encoding='utf-8', errors='ignore')
writer = csv.writer(fp)
'''title,salary,company,companyinfo,companyplace,place,exp,edu,num,time,info'''
writer.writerow(('职位', '薪资', '公司', '公司信息', '公司地址', '地区', '工作经验', '学历', '人数', '时间', '岗位信息'))


def parseInfo(url):
    headers = {
        'User-Agent': 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/ADR-1301071546) Presto/2.11.355 Version/12.10'
    }  # 更换请求头，防止被反爬虫
    res = requests.get(url, headers=headers)
    content = res.content.decode('utf-8')
    print("当前正在爬取:",url)
    print(content)
    res.encoding = 'utf-8'

    selector = etree.HTML(res.text)

    title = selector.xpath('//*[@id="pageContent"]/div[1]/div[1]/p/text()')
    salary = selector.xpath('//*[@id="pageContent"]/div[1]/p/text()')
    company = selector.xpath('//*[@id="pageContent"]/div[2]/a[1]/p/text()')
    companyinfo = selector.xpath('//*[@id="pageContent"]/div[2]/a[1]/div/text()')
    companyplace = selector.xpath('//*[@id="pageContent"]/div[2]/a[2]/span/text()')
    place = selector.xpath('//*[@id="pageContent"]/div[1]/div[1]/em/text()')
    exp = selector.xpath('//*[@id="pageContent"]/div[1]/div[2]/span[2]/text()')
    edu = selector.xpath('//*[@id="pageContent"]/div[1]/div[2]/span[3]/text()')
    num = selector.xpath('//*[@id="pageContent"]/div[1]/div[2]/span[1]/text()')
    time = selector.xpath('//*[@id="pageContent"]/div[1]/div[1]/span/text()')
    info = selector.xpath('string(//*[@id="pageContent"]/div[3]/div[2]/article)')

    pat = ' <p class="fp"><span class="label">职能类别：</span><a class="el tdn" href="https:.*?">(.*?)</a>'
    function1 = re.compile(pat,re.S).findall(content)
    print(function1)
    # 类选择器解析URL中对应HTML对应的字段内容
    info = str(info).strip()




    print(title, salary, company, companyinfo, companyplace, place, exp, edu, num, time, info)
    writer.writerow((title, salary, company, companyinfo, companyplace, place, exp, edu, num, time, info))


def getUrl(url):
    print('New page')
    res = requests.get(url)
    res.encoding = 'GBK'
    # print(res.text)
    if res.status_code == requests.codes.ok:
        selector = etree.HTML(res.text)
        urls = selector.xpath('//*[@id="resultList"]/div/p/span/a/@href')
        #                      //*[@id="resultList"]/div/p/span/a
        # id选择器找到当前网页每一个职位a标签对应的当前岗位具体信息URL列表
        print(urls)
        for url in urls:
            parseInfo(url)
            time.sleep(random.randrange(1, 4))
        # 设置线程休眠时间防止被反爬虫


if __name__ == '__main__':
    key = '心理学'
    # 第一页URL格式和后面的网页不一样
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,' + key + ',2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    getUrl(url)

    # 后页[2,100)
    urls = [
        'https://search.51job.com/list/000000,000000,0000,00,9,99,' + key + ',2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(
            i) for i in range(2, 2)]
    for url in urls:
        getUrl(url)

