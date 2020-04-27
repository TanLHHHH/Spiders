import requests
from lxml import etree
import lxml
import re
# url="http://landing.zhaopin.com/register?utm_source=baidupcpz&utm_medium=cpt&utm_provider=partner&sid=121113803&site=null"
#
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"} #添加浏览器头
# #你需要爬取的网页
# html=requests.get(url,headers=headers)
# html.encoding="utf-8"
# #print(html.text)
#
# html=etree.HTML(html.content, parser=etree.HTMLParser(encoding='utf-8'))               #etree.HTML():构造了一个XPath解析对象并对HTML文本进行自动修正。
# # #print(etree.tostring(html, encoding="utf-8").decode("utf-8"))
# # #将你的xpath复制到三引号里面，因为xpath里可能有双引号，所以我们加上三引号比较靠谱
# #s=html.xpath('''//*[@id="root"]/div[1]/div[1]/div/div/span[1]/span/text()''')
#
#
# #s = html.xpath('''//*[@id="root"]/div[2]/div[5]/div/button/text()''')
# # @ 获取标签内的属性
# s = html.xpath('''//*[@id="root"]/div[2]/div[5]/div/img/@alt''')
# print (s)		#一定要注意此种情况是未登录，即不需要cookies的情况，如果需要登陆则另说。

URL = "https://book.douban.com/top250"
res = requests.get(url=URL,headers=headers)
res.encoding = "utf-8"
html = etree.HTML(res.content,parser=etree.HTMLParser(encoding='utf-8'))

#获取书名

# XPATH
# s = html.xpath('''/html/body/div[3]/div[1]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[1]/a/@href''')
# print(s)

#正则
pat = '"<a href=".*?" onclick=".*?" title=(.*?)""> .*? </a>"'
s = re.compile(pat,re.S).findall(res.text)
print(s)
















