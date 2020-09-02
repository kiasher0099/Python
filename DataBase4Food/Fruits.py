#encoding:utf-8
#导入模块
import csv
import requests
import os

path = r"/Users/pro/Documents/VScode/Python/DataBase4Food/fruits_assets.csv"
#调用open()函数打开csv文件，传入参数：文件名“fruits_assets.csv”、追加模式“a”、newline=''。
with open(path, 'w', newline='') as csvfile:
    # 用csv.writer()函数创建一个writer对象。
    writer = csv.writer(csvfile, dialect='excel')
    header=['水果名称', '产地', '特征', '口感', '营养价值', '售价/100g']
    #用writerow()函数将表头写进csv文件里
    writer.writerow(header)

