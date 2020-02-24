file = open(r'D:\wangke\VS_CODE\python\风变编程\文件的读写\sources.txt','r', encoding='utf-8')          
file_lines = file.readlines()
file.close()

final_scores = [] 
# print(final_scores)
print(file_lines)

for i in file_lines:
    data = i.split()    
    sum = 0                    
    for score in data[1:]:     
        sum = sum + int(score)     
    result = data[0]+str(sum)+'\n'    
    final_scores.append(result)

print(final_scores)

winner = open(r'D:\wangke\VS_CODE\python\风变编程\文件的读写\winner.txt','w',encoding='utf-8') 
winner.writelines(final_scores)
winner.close()

print('===================排序后==================')

file1 = open(r'D:\wangke\VS_CODE\python\风变编程\文件的读写\winner.txt','r', encoding='utf-8')
file1_lines = file1.readlines()
file1.close()

dict_scores = {}
list_scores = []
final_scores_new = []

print(file1_lines)

for i in file1_lines:
    print(i)
    score = i[-4:-1]
    name = i[:-4]
    dict_scores[score] = name
    list_scores.append(score)

list_scores.sort(reverse=True)
print(list_scores)
print(dict_scores)

for i in list_scores:
    result = dict_scores[i] +':' + str(i) + '\n'
    final_scores_new.append(result)

print(final_scores_new)

# winner_new = open(r'D:\wangke\VS_CODE\python\风变编程\文件的读写\winner_new.txt','w', encoding='utf-8')
# winner_new.writelines(final_scores_new)
# winner_new.close()

with open(r'D:\wangke\VS_CODE\python\风变编程\文件的读写\winner_new.txt','w', encoding='utf-8') as winner_new:
    winner_new.writelines(final_scores_new)











