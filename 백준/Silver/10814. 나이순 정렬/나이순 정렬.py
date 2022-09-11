import sys

n = int(input())
dic = dict()

for i in range(n):
    dic[i] = list(map(str, sys.stdin.readline().rstrip().split()))

dic_sort = sorted(dic.items(), key=lambda x:int(x[1][0]))

for i in dic_sort:
    print(int(i[1][0]), i[1][1])
