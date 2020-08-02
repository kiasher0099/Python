import pandas as pd
import numpy as np

#  首先自己定义一些做测试的数据和表头
company, salary, address, experience, education, number_people = '北京知帆科技有限公司', '10.0k-18.0k', '北京-海淀区', '3-4年经验', '本科', '招3人'
data_list = (company, salary, address, experience, education, number_people)
#  tuple   list 类型都可以  区别：一个可变 一个不可变
# data_tuple = [company, salary, address, experience, education, number_people]
head = ('company', 'salary', 'address', 'experience', 'education', 'number_people')

"""
方法一   传入元组或者列表  
"""
# data = np.array([
#     [1, 2, 3, 4, 6, 6, 7],
#     [1, 2, 3, 4, 6, 6, 7]])
#  data  传入list  和 array类型都可以

df = pd.DataFrame(columns=head, data=list([data_list]))
# df = pd.DataFrame(columns=head, data=data)
df.to_csv('aa11.csv', mode='w', index=False, sep=',')

"""
方法二   传入字典
"""
# dic1 = {'company': ['北京知帆科技有限公司'], 'salary': ['10.0k-18.0k'], 'address': ['北京-海淀区'],
#         'experience': ['3-4年经验'], 'education': ['本科'], 'number_people': ['招3人']}
#  字典打包
dic = dict(zip(['company', 'salary', 'address', 'experience', 'education', 'number_people'],
               [[company], [salary], [address], [experience], [education], [number_people]]))

df = pd.DataFrame(columns=head, data=dic)
# df = pd.DataFrame(columns=head, data=dic1)
df.to_csv('aa22.csv', mode='w', header=True, index=False, sep=',')

"""
方法三  文件读写
"""
import codecs
import csv

# 文件读尽量用codecs.open方法，一般不会出现编码的问题。
f = codecs.open('aa33.csv', 'w', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(head)  # 写入表头  也就是文件标题
data_list = ['北京知帆科技有限公司', '10.0k-18.0k', '北京-海淀区', '3-4年经验', '本科', '招3人']
writer.writerow(data_list)

#  如果codes.open用不习惯的话    直接用with open
data_list = ['北京知帆科技有限公司', '10.0k-18.0k', '北京-海淀区', '3-4年经验', '本科', '招3人']
with open('aa44.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(head)  # 写入表头  也就是文件标题
    writer.writerow(data_list)