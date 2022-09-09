import sys

k = int(input())
lst = []

for _ in range(k):
    num = int(sys.stdin.readline())
    if num:
        lst.append(num)
    else:
        lst.pop()

print(sum(lst))
