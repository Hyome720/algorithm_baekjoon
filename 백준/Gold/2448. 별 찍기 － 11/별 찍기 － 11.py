import sys
from pprint import pprint

n = int(sys.stdin.readline().rstrip())
lst = [[' '] * (2 * n - 1) for _ in range(n)]

for i in range(n):
    for j in range(i + 1):
        lst[i][n - 1 + j] = '*'
        lst[i][n - 1 - j] = '*'

def star(x, y, t):
    if t == 3:
        lst[x + 1][y] = ' '
    else:
        for j in range(t // 2):
            for k in range(j + 1):
                lst[x + t - 1 - j][y + k] = ' '
                lst[x + t - 1 - j][y - k] = ' '

    da = [0, t // 2, t // 2]
    db = [0, -(t // 2), t // 2]

    for i in range(3):
        if 0 <= x + da[i] < n and 0 <= y + db[i] < 2 * n - 1 and t // 2 > 0:
            star(x + da[i], y + db[i], t // 2)


star(0, n - 1, n)

for i in lst:
    for j in i:
        print(j, end='')
    print()
