'''
Description: 
Version: Demo.0.0
Autor: Kiasher
Date: 2020-08-15 10:23:10
LastEditors: Kiasher
LastEditTime: 2020-08-16 11:10:11
'''
import requests

r = requests.get("http://www.baidu.com") 
print(r.status_code)
type(r)
r.headers
r.encoding
r.apparent_encoding
r.text

