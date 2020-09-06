'''
Description: 京东商品页面爬取的实例
Version: requests_01
Autor: Kiasher
Date: 2020-09-06 10:22:01
LastEditors: Kiasher
LastEditTime: 2020-09-06 12:02:14
'''

import requests
url = https://item.jd.com/100012015172.html#crumb-wrap
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬虫失败")


