import requests
import json
res = requests.get("http://www.4399.com")
# print(type(res))
# print(res.status_code)
# print(type(res.text))
# print((res.text))
# #print(res.cookies)

##返回的是二进制的内容 二进制的内容解码 避免出现乱码
#print(res.content)
# print(res.content.decode("utf-8"))
# #或者是
# res.encoding = "utf-8"
# print(res.text)
url = "http://www.jd.com"

# 文件上传
# file = {"file":open("filepath","rb")}
# res = requests.post(url=url,files=file)

#获取cookie
for key,value in res.cookies.items():
    print(key + "=" + value)

#会话维持 cookie 的一个作用就是可以用于模拟登陆 做会话维持
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456")
response = s.get("http://httpbin.org/cookies")
print(response.text)