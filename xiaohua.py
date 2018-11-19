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

USER_AGENT = [
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
]
HEADERS = {
        'User-Agent':random.choice(USER_AGENT),
}
IMG_HEADERS = {
        'User-Agent': random.choice(USER_AGENT),
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Host': 'img.gaoxiaogif.cn',
        'Cookie':'__cfduid=df2ee60aa9cdd483d44514b28ffe73e3a1542014149; Hm_lvt_07a40b1ea82034a3198f8530869191ca=1542013939,1542347444; Hm_lpvt_07a40b1ea82034a3198f8530869191ca=1542356815',
        'Connection':'keep-alive',
    }

MY_URL_TOU = 'http://www.gaoxiaogif.cn/gif/'
IMG_URL = 'http://n.sinaimg.cn/tech/transform/518/w207h311/20181116/rZGv-hnvukff6241151.gif'

def randomstrint():# 随机文件名
    return ''.join(random.sample(string.ascii_letters + string.digits, 8)) + '.gif'

def dir_folder(img_name):  # 判断是否有次文件夹，如果没有则创建  通用
    dir_img = 'img'  # 当前文件夹的文件名，这块应做成参数，更通用
    dir_name = os.path.join(os.getcwd(),dir_img)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return os.path.join(dir_name,img_name)

def download_gif(url,title='error'): #下载文件 处理数据库
    img_name = randomstrint() #获取随机生成的文件名字
    try:
        res = requests.get(url,timeout =300,stream = True,headers=HEADERS,)
        with open(dir_folder(img_name), 'wb') as fd:
            for chunk in res.iter_content(chunk_size = 65535):
                fd.write(chunk)
    except:
        print('{}异常'.format(url))
    print('下载完成')
    return url,title,img_name





# def savimg(url,filename):
#     pass
def myxiaohua(mypyq):  # 取出一页的数据函数
    if mypyq('.showlist li'):
        for item in mypyq('.showlist li').items():
            title_db = item('.showtxt').text()
            url_db = item('.lazy').attr('data-original')
            if title_db or url_db:
                time.sleep(2)
                print('*' * 100)
                print(title_db)
                print(url_db)
                print('正在下载')

                print('完成')
            else:
                print('*' * 100)
                print('王八犊子,空文件不存数据库')
    else:
        return False


for my_url_num in range(1, 2):  # 遍历所有页码并使用取出一页数据函数处理数据
    # print(my_url_num)
    my_url = MY_URL_TOU + str(my_url_num)
    time.sleep(random.uniform(2, 6))
    print(my_url)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        "Host": 'www.gaoxiaogif.cn',
    }
    r = requests.get(my_url, headers=headers)
    pyq = PyQuery(r.text)
    myxiaohua(pyq)
    if not myxiaohua(pyq):
        print('没有数据了 再见')
        break

