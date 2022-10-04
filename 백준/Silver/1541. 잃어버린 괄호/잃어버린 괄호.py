import sys

lst = sys.stdin.readline().rstrip().split('-')
res = []

for nums in lst:
    total = 0
    num = nums.split('+')
    for i in num:
        total += int(i)
    res.append(total)

n = res[0]
for i in range(1, len(res)):
    n -= res[i]
print(n)