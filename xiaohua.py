# -*- coding: utf-8 -*-
import os
# import sys
import requests
import urllib3
from urllib import request
from urllib import request as rq
# from PIL import Image
import time
# from bs4 import BeautifulSoup
from pyquery import PyQuery
import random
import string

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}
img_headers = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Host': 'img.gaoxiaogif.cn',
        'Cookie':'__cfduid=df2ee60aa9cdd483d44514b28ffe73e3a1542014149; Hm_lvt_07a40b1ea82034a3198f8530869191ca=1542013939,1542347444; Hm_lpvt_07a40b1ea82034a3198f8530869191ca=1542356815',
        'Connection':'keep-alive',

    }
img_headers2 = {

        'User-Agent': '"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"',

    }



MY_URL_TOU = 'http://www.gaoxiaogif.cn/gif/1'
IMG_URL = 'http://img.gaoxiaogif.cn/GaoxiaoGiffiles/images/2015/05/17/liangzhigoujiaopei.gif'

def randomstrint():# 随机文件名
    return ''.join(random.sample(string.ascii_letters + string.digits, 8)) + '.gif'

res_h =requests.get(MY_URL_TOU,headers=headers)

res = requests.get(IMG_URL,timeout =300,stream = True,headers=img_headers2,)
# size =res.headers.get('Range')
# print(size)

with open(randomstrint(), 'wb') as fd:
    for chunk in res.iter_content(chunk_size = 65535):
        if chunk:
            fd.write(chunk)

print('下载完成')

# def savimg(url,filename):
#     pass
# def myxiaohua(mypyq):  # 取出一页的数据函数
#     if mypyq('.showlist li'):
#         for item in mypyq('.showlist li').items():
#             title_db = item('.showtxt').text()
#             url_db = item('.lazy').attr('data-original')
#             if title_db or url_db:
#                 time.sleep(2)
#                 print('*' * 100)
#                 print(title_db)
#                 print(url_db)
#                 print('正在下载')
#
#                 print('完成')
#             else:
#                 print('*' * 100)
#                 print('王八犊子,空文件不存数据库')
#     else:
#         return False
#
#
# for my_url_num in range(1, 2):  # 遍历所有页码并使用取出一页数据函数处理数据
#     # print(my_url_num)
#     my_url = MY_URL_TOU + str(my_url_num)
#     time.sleep(random.uniform(2, 6))
#     print(my_url)
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
#         "Host": 'www.gaoxiaogif.cn',
#     }
#     r = requests.get(my_url, headers=headers)
#     pyq = PyQuery(r.text)
#
#     if not myxiaohua(pyq):
#         print('没有数据了 再见')
#         break

