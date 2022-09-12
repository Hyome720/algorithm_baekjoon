import sys

n = int(input())
lst = []
for _ in range(n):
    money = 0
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == b == c:
        money = 10000 + a * 1000
        lst.append(money)
    elif a == b:
        money = 1000 + a * 100
        lst.append(money)
    elif b == c:
        money = 1000 + b * 100
        lst.append(money)
    elif c == a:
        money = 1000 + c * 100
        lst.append(money)
    else:
        money = max(a, b, c) * 100
        lst.append(money)

print(max(lst))