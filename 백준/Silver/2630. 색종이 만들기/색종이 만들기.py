import sys

n = int(sys.stdin.readline().rstrip())
t = n
lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
white_total = 0
blue_total = 0

def paper(n, x, y):
    global white_total, blue_total
    if not n:
        return

    px = [0, 0, n, n]
    py = [0, n, 0, n]

    for s in range(4):
        blue_cnt = 0
        white_cnt = 0
        for j in range(n):
            for k in range(n):
                 if 0 <= x + px[s] + j < t and 0 <= y + py[s] + k < t:
                    if lst[x + px[s] + j][y + py[s] + k]:
                        blue_cnt += 1
                    else:
                        white_cnt += 1
        else:
            if blue_cnt and white_cnt:
                paper(n // 2, x + px[s], y + py[s])
            else:
                if blue_cnt:
                    blue_total += 1
                else:
                    white_total += 1

paper(n, 0, 0)

print(white_total - 3)
print(blue_total)
