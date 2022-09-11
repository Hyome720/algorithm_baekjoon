import sys

n, m = map(int, input().split())
lst = list(list(sys.stdin.readline().rstrip()) for _ in range(n))
cnt_lst = []
max_cnt = 0

for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if (k + l) % 2:
                    if lst[i + k][j + l] == 'W':
                        cnt += 1
                else:
                    if lst[i + k][j + l] == 'B':
                        cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
        cnt = 0
        for k in range(8):
            for l in range(8):
                if (k + l) % 2:
                    if lst[i + k][j + l] == 'B':
                        cnt += 1
                else:
                    if lst[i + k][j + l] == 'W':
                        cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)

print(64 - max_cnt)