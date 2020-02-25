import csv

with open(r'D:\wangke\VS_CODE\python\风变编程\模块的调用\CSV模块\test.csv','a', newline='',encoding='utf-8') as f:
    writer  = csv.writer(f)
    writer.writerow(['商品编号', '商品名称', '单价', '库存', '销售量'])
    writer.writerow(['1', '猫砂', '25', '1022', '886'])
    writer.writerow(['2', '猫罐头', '18', '2234', '3121'])