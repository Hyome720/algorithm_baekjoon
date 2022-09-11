import sys

n = int(input())
dic = dict()
res = []

for i in range(n):
    word = sys.stdin.readline().rstrip()
    dic[i] = [len(word), word]

dic_sort = sorted(dic.items(), key=lambda x:(x[1][0], x[1][1]))


for item in dic_sort:
    if item[1][1] not in res:
        res.append(item[1][1])

for i in res:
    print(i)
