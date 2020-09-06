'''
Description: 爬取亚马逊商品页面
Version: request_02
Autor: Kiasher
Date: 2020-09-06 11:19:17
LastEditors: Kiasher
LastEditTime: 2020-09-06 12:01:09
'''
import requests
url = "https://www.amazon.cn/dp/B07TKM6S4C"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    print(r.request.headers)
    # 可以先看下所有的返回值，因为如果用 r.text[:1000] 来切片看片段的信息可能不知道具体返回的信息是正确的还有有问题的
    print(r.text) 
except:
    print("爬虫失败")
