'''
Description: 百度/360搜索关键字
Version: request_03
Autor: Kiasher
Date: 2020-09-06 11:19:17
LastEditors: Kiasher
LastEditTime: 2020-09-06 12:01:00
'''
import requests
url = "http://www.baidu.com/s"
keyword = "Python"
try:
    kv = {'wd':keyword}
    r = requests.get(url,params=kv)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    print(r.request.headers)
    # 一般搜索返回的字符串会很长，这里可以简单看下返回值得长度
    print(len(r.text))
except:
    print("爬虫失败")
