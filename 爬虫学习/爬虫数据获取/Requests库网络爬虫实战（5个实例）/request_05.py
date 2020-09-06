'''
Description: IP地址归属地的自动查询
Version: request_05
Autor: Kiasher
Date: 2020-09-06 11:19:17
LastEditors: Kiasher
LastEditTime: 2020-09-06 12:14:57
'''
import requests
url = "https://www.ip138.com/iplookup.asp?ip="
ip = '202.204.80.112&action=2'
try:
    r = requests.get(url+ip)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    print(r.request.headers)
    # 用 r.text[-500:] 查看返回值的后500个字符
    print(r.text[-500:]) 
except:
    print("爬虫失败")
