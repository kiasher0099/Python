import csv

with open(r'D:\wangke\VS_CODE\python\风变编程\模块的调用\CSV模块\test.csv', newline = '', encoding = 'utf-8')  as f:
    #参数encoding = 'utf-8'防止出现乱码
    reader = csv.reader(f)
    #使用csv的reader()方法，创建一个reader对象
    for row in reader: 
    #遍历reader对象的每一行
        print(row)

print("读取完毕！")