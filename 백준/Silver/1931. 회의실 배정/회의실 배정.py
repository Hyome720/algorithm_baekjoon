import sys

n = int(input())
dic = dict()
res = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dic[i] = (a, b)

dic = sorted(dic.values(), key=lambda x:(x[1], x[0]))

for i in range(n):
    if not i:
        res.append(dic[i])
    elif dic[i][0] >= res[-1][1]:
        res.append(dic[i])

print(len(res))

