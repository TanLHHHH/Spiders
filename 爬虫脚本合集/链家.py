#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 17:38
# @Author  : TanLHHH
# @Site    : 
# @File    : 链家.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv
import time
import threading


class  lianjiaspider(object):
    def __init__(self):
        # 链家首页的链接
        self.home_url='http://bj.lianjia.com/'
        # 用户的登陆界面，登陆后为链家首页的界面
        self.auth_url='https://passport.lianjia.com/cas/login?service=http%3A%2F%2Fbj.lianjia.com%2F'
        self.zaishou_url='https://su.lianjia.com/ershoufang/pg{}/'
        self.headers=headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'su.lianjia.com',
    'Referer': 'https://su.lianjia.com/chengjiao/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'XMLHttpRequest',

}


    def main_url(self,page):#生成在售房屋每一页的URL
        #r=requests.get(self.home_url)
        #return r.text
        for next_page in range(1,int(page)):
            yield self.zaishou_url.format(next_page)#,可以用于迭代

    def detail_sall_url(self):
        user_num = input('请输入你想要的主页的页数：')
        detail_url_list = []
        for i in self.main_url(str(int(user_num)+1)):
            try:
                response=requests.get(i,headers=self.headers)
                if response.status_code==200:#一定不能加引号啊，不然怎么都匹配不到的
                    html=response.text
                    soup=BeautifulSoup(html,'lxml')
                    detail_a_label=soup.select('.clear .noresultRecommend')#返回的是一个列表
                    for each_a_label in detail_a_label:
                        detail_url_list.append(each_a_label['href'])#获得标签，然后获取属性href ，并依次取出详情页的标签把他放在一个列表当中
            except requests.ConnectionError as e:
                print ('error:', e.args)
        return detail_url_list


    def parse_detail_url(self,detail_url_list):#用于解析详情页
        info_concat=[]
        for each_detail_url in detail_url_list:
            response_detail=requests.get(each_detail_url)
            if response_detail.status_code==200:
                html_detail_url=response_detail.text
                info={}#存为字典/json 形式
                soup=BeautifulSoup(html_detail_url,'lxml')
                info1=soup.select('.title .main')#获取含有标题的标签的列表
                for  j in  info1:
                    info['出售房屋标题']=j.get_text()#获取标题
                info2=soup.select('.price .total')#获取房屋价格
                for p in info2:
                    info['总价']=p.string + '万'
                info3 = soup.select('.unitPriceValue')  # 获取房屋每平方均价
                for unit_price in info3:
                    info['平方售价'] = unit_price.get_text()
                info4 = soup.select('.room')  # 获取厅室
                for property in info4:
                    info['房屋属性'] = property.get_text()
                info5 = soup.select('.area')
                for areas in info5:
                    info['面积'] = areas.get_text()
                info6 = soup.select('.type')
                for areas in info6:
                    info['朝向'] = areas.get_text()
                    info_concat.append(info)
            else:
                print ('error:', requests.ConnectionError)
        return info_concat


    def save_to_xlsx(self,detail_url_list): #用于将数据存储到 excel 当中
        pass
        #BeautifulSoup.DataFrame(self.parse_detail_url(detail_url_list)).to_excel('链家二手房.xlsx', sheet_name='链家二手房信息')


def main():
    lianjia=lianjiaspider()#实例化
    detail_url_list=lianjia.detail_sall_url()#获取详情页
    #打印信息
    print(lianjia.parse_detail_url(detail_url_list))
    #保存至xlsx
    lianjia.save_to_xlsx(detail_url_list)


if __name__=='__main__':
    main()
