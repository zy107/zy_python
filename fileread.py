# -*- coding: utf-8 -*-
#读取
a = open('班级.csv',encoding="gbk")
k=[]
for i in a:
    i = i.replace('\n','')
    k.append(i.split(','))
print(k)
#总分
z = open('总分.csv','w+',encoding="gbk")
for i in  range(len(k)):
    sum_score = 0
    if i == 0:
        k[i].append('总分')

    for j in range(len(k[i])):
        if k[i][j].isnumeric() and (k[0][j]=='文综' or k[0][j]=='理综'):
            sum_score += int(k[i][j])
    k[i].append(str(sum_score))
    z.writelines(k[i][0]+','+k[i][1]+','+k[i][2]
                        +','+k[i][3]+','+k[i][4]+'\n')

scors = []
for t in range(1,len(k)):
    scors.append(k[t][-1])

rank=[k[0]]
sorted_id = sorted(range(len(scors)), key=lambda k: scors[k], reverse=True)
for r in range(len(sorted_id)):
    rank.append(k[sorted_id[r]+1])
#写入文件
x = open('排序.csv','w+',encoding="gbk")
for i in  range(len(rank)):
    x.writelines(rank[i][0]+','+rank[i][1]+','+rank[i][2]
                        +','+rank[i][3]+','+rank[i][4]+'\n')
a.close()
z.close()
x.close()