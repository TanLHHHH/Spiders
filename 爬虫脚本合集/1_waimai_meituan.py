# -*- coding: utf-8 -*-
import base64
import binascii
import json
import random
import re
import time
import zlib

import execjs
import pymongo
import requests


proxy_user_pass = "ZESHUNI6BF0OSL0:JRQOgdPX"
proxy = 'http-proxy-t1.dobel.cn:9180'
encoded_user_pass = "Basic " + base64.urlsafe_b64encode(bytes((proxy_user_pass), "ascii")).decode("utf8")
proxies = {
    # "http":"http://{}".format(proxy),
    'http':proxy
}
def get_token():
    """
    生成加密的token
    :return:
    """
    now = int(time.time() * 1000)
    ip = {
        "rId": "100043",
        "ver": "1.0.6",
        "ts": now,
        "cts": now,  # 保证比ts大
        "brVD": [1920, 640],
        "brR": [[1920, 1080], [1920, 1040], 24, 24],
        "bI": [
            'https://epassport.meituan.com/account/unitivelogin?bg_source=6&service=movie&continue=https://e.maoyan.com/backend/account/user/entry/merchant',
            'https://e.maoyan.com/user/login?next=%2F'],
        "mT": ["133,191", "133,192", "132,193", "131,194", "131,195", "130,197", "128,198", "127,200", "126,200",
               "124,202", "124,203", "123,204", "121,204", "120,206", "119,206", "118,207", "118,208", "117,208",
               "117,209", "116,210", "115,211", "114,214", "114,215", "113,215", "111,218", "110,220", "107,225",
               "13,143", "32,139", "53,136"],
        "kT": ["18,INPUT", "V,INPUT", "17,INPUT", "18,INPUT", "V,INPUT", "17,INPUT", "{,INPUT"],
        "aT": ["133,191,BUTTON", "150,125,INPUT", "96,76,INPUT", "119,88,INPUT", "158,25,A", "230,30,A",
               "118,127,INPUT", "132,93,INPUT", "72,85,INPUT", "102,32,A"],
        "tT": [],
        "aM": "ps",
    }
    info = json.dumps(ip, separators=(',', ':')).encode('utf-8')
    token = base64.b64encode(zlib.compress(info)).decode('utf-8')
    return token

def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """

    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    """
    处理使用PKCS7填充过的数据
    :param text: 解密后的字符串
    :return:
    """
    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]


def encrypt(key, content):
    """
    AES加密
    key,iv使用同一个
    模式cbc
    填充pkcs7
    :param key: 密钥
    :param content: 加密内容
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes

    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # 重新编码
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result

def get_headers():
    headers={
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://h5.waimai.meituan.com",
        "Referer": "https://h5.waimai.meituan.com/waimai/mindex/home",
        "Sec-Fetch-Mode": "cors",
        'Proxy-Authorization': encoded_user_pass,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        'Cookie':'_lxsdk_cuid=16ed1588dcdc8-00f191d5b06a3-6b131a7b-1fa400-16ed1588dcec8; iuuid=AF554F442EF442A496FDABFE0382EAACDCA19F97FD7D83373E557ECBAFFE4375; cityname=%E6%9D%AD%E5%B7%9E; _hc.v=ea91d17a-39a1-fba6-5adc-a2bcfdba04d9.1575513054; _lxsdk=AF554F442EF442A496FDABFE0382EAACDCA19F97FD7D83373E557ECBAFFE4375; _ga=GA1.3.649988102.1577449864; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=207994541.1577449865726.1578658070811.1586063354012.5; wm_order_channel=default; utm_source=; au_trace_key_net=default; openh5_uuid=AF554F442EF442A496FDABFE0382EAACDCA19F97FD7D83373E557ECBAFFE4375; uuid=AF554F442EF442A496FDABFE0382EAACDCA19F97FD7D83373E557ECBAFFE4375; service-off=0; showTopHeader=show; userId=686369053; userId=686369053; userName=%E5%8D%81%E4%B9%9D%E5%85%AB%E4%B8%83216; userFace=https://img.meituan.net/avatar/cc5e1f666d0d0a6b626847382a2cae4e6130.jpg; token=3nhiUZ81GpSQc9kWZnvbtErmJr0AAAAAWgoAAJenD30UQhuZXzJsN0D_0waDtaIVLhgkMZXALC-pqZEPtm1_B7Vunm4CwhaKEZZudA; mt_c_token=3nhiUZ81GpSQc9kWZnvbtErmJr0AAAAAWgoAAJenD30UQhuZXzJsN0D_0waDtaIVLhgkMZXALC-pqZEPtm1_B7Vunm4CwhaKEZZudA; oops=3nhiUZ81GpSQc9kWZnvbtErmJr0AAAAAWgoAAJenD30UQhuZXzJsN0D_0waDtaIVLhgkMZXALC-pqZEPtm1_B7Vunm4CwhaKEZZudA; cssVersion=c887f9a6; _lxsdk_s=1714e8c5f49-8be-46d-fd2%7C686369053%7C1'
    }
    return headers

def parse(formdata):
    poi_name=formdata['poi_name']
    wm_latitude=formdata['wm_latitude']
    wm_longitude=formdata['wm_longitude']
    wm_actual_latitude=formdata['wm_actual_latitude']
    wm_actual_longitude=formdata['wm_actual_longitude']
    data_param =  {
        "startIndex": 0,
        "sortId": "0",
        "multiFilterIds": "",
        "sliderSelectCode": "",
        "sliderSelectMin": "",
        "sliderSelectMax": "",
        "geoType": "2",
        "rankTraceId": "",
        "uuid": "AF554F442EF442A496FDABFE0382EAACDCA19F97FD7D83373E557ECBAFFE4375",
        "platform": "3",
        "partner": "4",
        "originUrl": "https://h5.waimai.meituan.com/waimai/mindex/home",
        "riskLevel": "71",
        "optimusCode": "10",
        "wm_latitude": wm_latitude,
        "wm_longitude": wm_longitude,
        "wm_actual_latitude": wm_actual_latitude,
        "wm_actual_longitude": wm_actual_longitude,
        "openh5_uuid": "AF554F442EF442A496FDABFE0382EAACDCA19F97FD7D83373E557ECBAFFE4375",
        "_token": "eJx9UNlum1AU/Bek9MWWAYNZLEUV2Masjs1igqOoYrnsmwGbpeq/97pJ1Jeq0pFmztwZndH9iTRSgKxxDKcxfI7cQYOsEXyBLShkjnQtfFkxFEatCIZgaGaO+H81iqAohoSa15y3yPqNxMk5TVDvD0GH+xvOLrE5jjHY+/yLk5AvSTgPlwRNSNx1dbtG0Xi16N2kcJNFAZLu5pYLvyrQDwktkjIAAxpXBYC1/h/Jqygpv4dV44PnrrmBb57rZz9uTf78J/dEcE9LAc4/01D/ECH5OPpwPs7CwoUJC0PMPtH9xO5r1+DfwX5tEpWQAXnssm1370fOikNW5RnPue/GapC40JBF9woyX7rc9wrntKl8x4iVn1mdvqRLRaTZSbyBsHY1deZOzobzgpfRqGhZPxD9KHOFhIWULQS0scmq+lSdcp5QL2pvNPZ4zpdyRyVmW2TexisTU7VbwlY1f+fX1Kp2lc7Sp30M8uvg5aOj6S1nxPvkiDeoaDh9PfndZDkD5rOe7XrdMFwv5xmGha+iIMbeYabJQbLVKM72w8zUT7tJPryI446KLNFCG+N4SwF9MrZAcT0laVwyT1+zq2D37iSkmaDjk76RgrRgix0zbU4er3UlP2z9qTDpgDhiSYM2I48n4cmJanFs+KxRLkRw9qYbi0bplY5m9ISyWhyuwHaUyD7mdLs8ElaUokB3okg9F7h8DnHNkapY7k0gvRxfWzJWpr1gsrPyLlM88us31uX0+A==",
    }

    while True:
        ts = str(int(time.time() * 1000))
        cts = str(int(time.time() * 1000))
        xforwity = '{"ts":' + ts + ',"cts":' + cts + ',"brVD":[375,812],"brR":[[375,812],[375,812],24,24],"aM":"","code":"20200405172737326-4927978-TyqxKGHPiwiK"}'
        xforwity_enc = encrypt('jvzempodf8f9anyt', xforwity)
        print(xforwity_enc)
        params = "_={timestamp}&X-FOR-WITH={xforwith}".format(timestamp=int(time.time() * 1000), xforwith=xforwity_enc)
        for c in params.split('&'):
            data_param[c.split('=')[0]]=c.split('=')[-1]
        data_param['_token']= get_token()
        url = "https://i.waimai.meituan.com/openh5/homepage/poilist?"
        headers = get_headers()
        res = requests.post(url=url+params.format(), headers=headers, data=data_param,verify=False
                            ,proxies=proxies
                            )
        print(data_param)
        text = parse_decode(res.text)
        json1 = json.loads(text)
        print('页数：',data_param['startIndex'],'--',json1)
        if '请先登录' in json1['msg']:
            pass
            time.sleep(2)
        else:
            data = json1['data']
            rankTraceId = data['judasData']['rankTraceId']
            shop_list = data['shopList']
            for shop_item in shop_list:
                shop_item['poi_name']=poi_name
                insert_mongo(shop_item)
            data_param['rankTraceId'] = rankTraceId
            data_param['startIndex'] = data['nextStartIndex']
            if rankTraceId =='':
                break
            time.sleep(2)



# MongoDB配置
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DATABASE = 'data'
client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
db = client[MONGODB_DATABASE]
cusor = db['kb_meituan_waimai']
def insert_mongo(item):
    try:
        cusor.insert(item)
    except:
        pass

def parse_decode(text):
    """
    woff字体解析
    :param text:
    :return:
    """
    unicode_list=[
        'uniF717', 'uniE5B4', 'uniE34A', 'uniE674', 'uniEA28', 'uniE57F', 'uniF437', 'uniE7D0', 'uniEB50', 'uniE3EF',#4045
        'uniE281', 'uniF7EA', 'uniE7F9', 'uniE0B2', 'uniF895', 'uniEFCF', 'uniE57A', 'uniF5A9', 'uniF064', 'uniEEF2',#163d
        'uniEA5C', 'uniF167', 'uniEF9E', 'uniE063', 'uniE3B9', 'uniE1FD', 'uniF4D8', 'uniE469', 'uniEC35', 'uniF5A4',#f616
        'uniEA72', 'uniE1A8', 'uniF585', 'uniEA6E', 'uniF666', 'uniF7F2', 'uniE526', 'uniF866', 'uniE776', 'uniE26E',#f94a
        'uniEAF0', 'uniE868', 'uniF0A1', 'uniF154', 'uniEB21', 'uniE7A8', 'uniE0B7', 'uniE366', 'uniECE7',  'uniE745'#c887f
                   ]
    decode_list=[
        '1','6','7','9','8','2','5','4','0','3',
        '8','4','3','7','2','0','6','5','9','1',
        '1','4','2','8','3','5','7','6','0','9',
        '8','1','3','0','8','7','5','9','2','6',
        '9','6','8','7','2','5','4','1','0','3',
                 ]
    compile_rule_unicode = re.compile(r'&#x([a-zA-Z0-9]+);', re.S)
    re_unicode = re.findall(compile_rule_unicode, text)
    for tag_uni in re_unicode:
        tag_name = "uni" + tag_uni.upper()
        index = unicode_list.index(tag_name)
        tag_value = decode_list[index]
        if tag_value is not None:
            text = text.replace('&#x{};'.format(tag_uni),
                                          '{}'.format(tag_value))
    return text

if __name__ == '__main__':
    list1 =[
        {"wm_latitude": "25119941",
         "poi_name":'新乐小区29号楼',
        "wm_longitude": "99170351",
        "wm_actual_latitude": "31141697",
        "wm_actual_longitude": "121507684"},
        {"wm_latitude": "24820560",
         "poi_name": '昌宁人民医院',
         "wm_longitude": "99616800",
         "wm_actual_latitude": "31228428",
         "wm_actual_longitude": "121478223"}
        ]
    for data in list1:
        parse(data)