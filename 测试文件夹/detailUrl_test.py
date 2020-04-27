#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 10:16
# @Author  : TanLHHH
# @Site    : 
# @File    : detailUrl_test.py
# @Software: PyCharm
from http.cookies import SimpleCookie

import requests

def cookie_parser():
    cookie_string= 'zguid=23|%246357d797-c41c-4518-99bf-418c1b61ef8c; zgsession=1|d0ecdab5-74da-4911-9e6e-60517e759d28; _ga=GA1.2.1019427332.1584684752; _gid=GA1.2.337213944.1584684752; _pxvid=c826cbe3-6a71-11ea-aa45-0242ac12000b; zjs_user_id=null; zjs_anonymous_id=%226357d797-c41c-4518-99bf-418c1b61ef8c%22; _gcl_au=1.1.75950928.1584684754; KruxPixel=true; DoubleClickSession=true; _fbp=fb.1.1584684754632.698330712; KruxAddition=true; __gads=ID=bd1953a279722338:T=1584685340:S=ALNI_MYC1jYeTR-y5nWH2L2sH-0G1X8QHQ; ki_r=; ki_s=199442%3A0.0.0.0.0; FSsampler=1344456025; GASession=true; JSESSIONID=491498A0403EF2A34DF9978E6750A834; AWSALB=bFIYxMJiOXLZvIFpCEqKBrZ0e5lHfWTvGRN0nn0Cg8is3Vf1k2CdRtovh6p8YGzchZj+IJkhYgY6mEOhpLXcZktEKYu/heWypIGUF/b3J9HYjkp67V3C/fl8th+M; AWSALBCORS=bFIYxMJiOXLZvIFpCEqKBrZ0e5lHfWTvGRN0nn0Cg8is3Vf1k2CdRtovh6p8YGzchZj+IJkhYgY6mEOhpLXcZktEKYu/heWypIGUF/b3J9HYjkp67V3C/fl8th+M; search=6|1587283584551%7Crect%3D37.842913%252C-122.329919%252C37.707608%252C-122.536739%26rid%3D20330%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%09%01%0920330%09%09%09%090%09US_%09; _px3=cedd9fa9f24bb1588d2f1b456d6afe2521ae66beceb2c90c28d988e2f04b76e3:74VNUxO7MtyRgTkvhz+OLYquFvs9vOKa+S6DEHMOvscP+hJTcxDuIyD/nyACz/SILqOPpmJEqGOnzn4kov82TA==:1000:OEOxD4ZwCYzbxGv/KNSZcv3s6C1hdC20Bhi7rskQrZl8ifvswtrJ+5fmD80Akc8v7ZJoLTndEUiDmLZ5iH13Ey3Eh5vHl1p3EINmv/huPiv+9BJYZ2m600aZg0F0A1ei9NFPF6sulrOleI0Vx91F2J/qzYWBzHtdqkv1lwROvW0=; _gat=1; ki_t=1584685344640%3B1584685344640%3B1584691741227%3B1%3B305'
    cookie=SimpleCookie()
    cookie.load(cookie_string)

    cookies= {}

    for key, morsel in cookie.items():
        cookies[key]= morsel.value

    return cookies



url = "https://www.zillow.com/b/hanover-midtown-atlanta-ga-BMVS7Z/"
#
# headers = {
# #":authority": "www.zillow.com",
# #":method": "GET",
# #":path": "//b/piedmont-house-atlanta-ga-5hWBqm/",
# #":scheme": "https",
# "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "accept-encoding": "gzip, deflate, br",
# "accept-language": "zh-CN,zh;q=0.9",
# #"cache-control": "max-age=0",
# "cookie": """zguid=23|%24219996ee-44dc-4cb4-8f37-fc8e78573c21; _ga=GA1.2.1032167391.1585101484; _gid=GA1.2.289146351.1585101484; zjs_user_id=null; zjs_anonymous_id=%22219996ee-44dc-4cb4-8f37-fc8e78573c21%22; _pxvid=11e786b6-6e3c-11ea-b868-0242ac12000b; _gcl_au=1.1.343300040.1585101491; KruxPixel=true; _fbp=fb.1.1585101498212.1379542854; KruxAddition=true; ki_r=; ki_s=199442%3A0.0.0.0.0; optimizelyEndUserId=oeu1585128963262r0.9895900366700423; G_ENABLED_IDPS=google; JSESSIONID=C913E3F4D26844CFA8B04E5539D60314; zgsession=1|fa0a068b-3783-4bf1-acc5-7f817bc58500; DoubleClickSession=true; ki_t=1585105365055%3B1585185272333%3B1585187016545%3B2%3B490; _px3=659aee0289b4ae7924049ba27fbadeea7b2d6f6a1a98563701f3275263cbc954:6CdjWN51HGN1W1NB7QMwMnSGvJz55DwIfvBJNMBThnNUVzYkW64+4Jp+fSUojEMAMUgu8LAaH1hPldcEWfIyBw==:1000:nlK2V8JJp/os/vN9gMpH6egQITGWYCRNL/LxPvX0uP3D6Kl4GGwMIVooKztTNNsuf3Ukk929gY1EdjhqyIv34of/PEv8tO4RuQ2wsyD63MaACBjHEtYMkv/qkAdZ/hdxZTBRvfGRR+iGJoXn46kah+XVFapNtlWSlUt2+f3LXIc=; AWSALB=Nu5an5xRzfmWO5Km5rm4/e7scwGXLaDR+irlA3jdKpbx3VP7vQPYXidFOla8r2+Wu3i1jVtxbM11mPpoqQUlinQfoAvj6jPfxs9NGBHQVofFxuR/nh09a4oUtQyD; AWSALBCORS=Nu5an5xRzfmWO5Km5rm4/e7scwGXLaDR+irlA3jdKpbx3VP7vQPYXidFOla8r2+Wu3i1jVtxbM11mPpoqQUlinQfoAvj6jPfxs9NGBHQVofFxuR/nh09a4oUtQyD; search=6|1587779123068%7Crect%3D33.84582550452954%252C-84.28427696228027%252C33.72226941499438%252C-84.47688102722168%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D0%26type%3Dcondo%252Capartment_duplex%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%09%096181%09%09%09%09%09%09
# """,
# "Host": "www.zillow.com",
# #"sec-fetch-dest": "document",
# #"sec-fetch-mode": "navigate",
# #"sec-fetch-site": "none",
# #"sec-fetch-user": "?1",
# "upgrade-insecure-requests": "1",
# "user-agent": "Mizilla/5.0",
# "refer":"www.zillow.com"
# }

headers= {
					'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
					'accept-encoding':'gzip, deflate, sdch, br',
					'accept-language':'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
					'cache-control':'max-age=0',
					'upgrade-insecure-requests':'1',
					'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
		}

res = requests.get(url=url,headers=headers)
print(res.text)