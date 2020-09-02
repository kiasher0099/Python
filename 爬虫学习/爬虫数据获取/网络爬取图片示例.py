'''
Description: 通过特定的URL地址从网页爬取图片，后续可补充爬取动画，音视频的代码。注意这些文件都为二进制文件。
Version: Demo.0.0
Autor: Kiasher
Date: 2020-08-22 11:32:11
LastEditors: Kiasher
LastEditTime: 2020-08-22 11:44:39
'''

import requests
import os 

url = input("请输入想要爬取的URL地址：")
root = "D://爬虫学习//"
path = root + url.split('%')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exitst(path):
        r = requests.get(url)
        r.status_code
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close
            print("文件保存成功！")
    else:
        print("文件已存在")
except:
    print("爬取失败...")
