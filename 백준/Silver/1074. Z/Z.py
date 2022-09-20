import sys

def Zet(n):
    global res, a, b
    if n < 1:
        return
    x = a // (2 ** (n - 1))
    y = b // (2 ** (n - 1))
    a = r % (2 ** (n - 1))
    b = c % (2 ** (n - 1))

    if x and y:
        res += 2 ** (2 * n - 2) * 3
    elif x:
        res += 2 ** (2 * n - 2) * 2
    elif y:
        res += 2 ** (2 * n - 2)
    else:
        res += 0
    Zet(n - 1)

n, r, c = map(int, sys.stdin.readline().rstrip().split())
a, b = r, c
res = 0

Zet(n)
print(res)


