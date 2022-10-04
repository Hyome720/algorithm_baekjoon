import sys

n = int(sys.stdin.readline().rstrip())
lst = list(list(sys.stdin.readline().rstrip()) for _ in range(n))
res = []

total_zero = 0
total_one = 0


def quad(x, y, n):
    check_num = lst[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if lst[i][j] != check_num:
                res.append('(')
                for k in range(2):
                    for l in range(2):
                        quad(x + k * n // 2, y + l * n // 2, n // 2)
                res.append(')')
                return
    res.append(check_num)





quad(0, 0, n)

for i in res:
    print(i, end='')
