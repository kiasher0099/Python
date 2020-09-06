'''
Description: 网络图片的爬取和储存
Version: request_04
Autor: Kiasher
Date: 2020-09-06 11:19:17
LastEditors: Kiasher
LastEditTime: 2020-09-06 12:00:51
'''
import requests
import os
url = "https://www.natgeoexpeditions.com.au/content/images/static/Hero-interest-wildlife.jpg"
root = "D://爬虫学习//"
# 截取URL地址以'/'为分割符的最后一个字段
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬虫失败")
