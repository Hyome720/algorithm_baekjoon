def final(n):
    global cnt
    if n == 1:
        return res
    for i in range(n // 3 + 1, n // 3 + n // 3 + 1):
        for j in range(n // 3 + 1, n // 3 + n // 3 + 1):
            for k in range(0, t + 1, n):
                for l in range(0, t + 1, n):
                    if i + k < t + 1 and j + l < t + 1:
                        res[i + k][j + l] = blank
    else:
        cnt += 1
        final(n // 3)
        return res


n = int(input())
cnt = 0
t = n
blank = ' '
res = [[0] * (n + 1)] + [[0] + ['*'] * n for _ in range(n)]

final(n)

# for i in range(1, n + 1):
#     print(*res[i][1:])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if res[i][j] == 0:
            pass
        else:
            print(res[i][j], end='')
    else:
        print()