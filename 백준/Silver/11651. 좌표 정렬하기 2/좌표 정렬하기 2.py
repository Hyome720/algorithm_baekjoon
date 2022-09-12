import sys

n = int(input())
dic = dict()

for i in range(n):
    dic[i] = list(map(int, sys.stdin.readline().rstrip().split()))

dic_sort = sorted(dic.items(), key=lambda x:(x[1][1],x[1][0]))

for item in dic_sort:
    print(*item[1])
