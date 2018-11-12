# -*- coding: utf-8 -*-

import requests
# from PIL import Image
from bs4 import BeautifulSoup


my_url_tou = 'http://www.gaoxiaogif.cn/gif/'
my_url_num = 22
my_url = my_url_tou + str(my_url_num)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    "Host": 'www.gaoxiaogif.cn',

}
r = requests.get(my_url,headers=headers)

b = BeautifulSoup(r.text,'lxml')


print(r.status_code,'----',b.p.span.text)
