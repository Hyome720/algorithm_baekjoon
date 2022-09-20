import sys

def plus(k):
    if k == n:
        return lst
    else:
        lst.append(lst[k - 3] + lst[k - 2] + lst[k - 1])
        plus(k + 1)


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    lst = [1, 2, 4]
    n = int(sys.stdin.readline().rstrip())
    if n > 3:
        plus(3)
        print(lst[-1])
    else:
        print(lst[n - 1])