import sys

n = input()
dic = dict()
for i in range(len(n)):
    dic[i] = n[i]

dic_sort = sorted(dic.items(), key=lambda x:x[1], reverse=True)

for i in dic_sort:
    print(i[1], end="")