list_test = ['只是当时已惘然。','此情可待成追忆，\n']  # 将要默写的诗句放在列表里。
with open ('D:\wangke\VS_CODE\python\风变编程\文件读写实例\poem.txt','r', encoding='utf-8') as f:
    lines = f.readlines()
print(lines)

with open('D:\wangke\VS_CODE\python\风变编程\文件读写实例\poem1.txt','w', encoding='utf-8') as new:
    for line in lines:
        if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
            new.write('____________。\n')
        else:
            new.write(line)
           
