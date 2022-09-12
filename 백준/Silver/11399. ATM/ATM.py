import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
dic = dict()
time = 0

for i in range(len(lst)):
    dic[i] = lst[i]

dic_sort = sorted(dic.items(), key=lambda x:x[1])

for i in range(n):
    time += dic_sort[i][1] * (n - i)

print(time)

