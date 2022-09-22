import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
broken = list(map(int, sys.stdin.readline().rstrip().split()))

dic = dict()
dic[100] = 0
min_cnt = abs(100 - n)

btn = [i for i in range(10)]

for i in broken:
    btn.remove(i)

for num in range(1000001):
    for i in str(num):
        if int(i) in btn:
            pass
        else:
            break
    else:
        min_cnt = min(min_cnt, len(str(num)) + abs(n - num))

print(min_cnt)