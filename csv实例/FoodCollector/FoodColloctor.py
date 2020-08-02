'''
@Description: Collocting food (or just fruits) infomation from Websites and store it into a csv file.
@Version: Demo.0.0
@Autor: Kiasher
@Date: 2020-07-30 21:46:53
@LastEditors: Kiasher
@LastEditTime: 2020-08-01 12:04:07
'''

import io
import csv
#调用csv模块


header=['水果名称', '种类', '成熟周期', '甜度', '酸度', '涩度', '营养价值', '备注']


with open(r'D:\VScode\Python\csv实例\FoodCollector\foodcolloctor.csv', 'w', encoding='gbk', newline='') as fc:
#调用open()函数打开csv文件，传入参数：文件名“foodcolloctor.csv”、追加模式“a”、newline=''。
    writer = csv.writer(fc, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。

    writer.writerow
