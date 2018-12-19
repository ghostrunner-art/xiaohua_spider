# -*- coding: utf-8 -*-
import oss2

from mypath.myfilepath import Mypath
import requests

version = oss2.__version__
print('阿里oss版本:', version)

mypath = Mypath('img')  # 实例化路径类,如无参数目录则创建
auth = oss2.Auth('LTAI3JGE6IStAzfq', 'XkOvBDmQVbBU8yPjNUL5t5NTGpEb5g')
endpoint = 'http://oss-cn-zhangjiakou.aliyuncs.com'

bucket = oss2.Bucket(auth, endpoint, 'xiaohuatest',connect_timeout=30)

# service = oss2.Service(auth,endpoint)

name_cloud, name_local = mypath.filename_path('16.jpg')




















# bucket.create_bucket(oss2.models.BUCKET_ACL_PUBLIC_READ) # 创建bucket并指定权限

bucket.put_object_from_file(name_cloud, name_local)  # 上传文件，如果文件名重复不报错，会覆盖

