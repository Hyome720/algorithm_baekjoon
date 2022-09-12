import sys

def sequence(idx, n, m, res):
    if idx == m:
        print(*res)
        return

    start = 1
    if res:
        start = max(res) + 1
    for i in range(start, n + 1):
            res.append(i)
            sequence(idx + 1, n, m, res)
            res.pop()


n, m = map(int, input().split())

sequence(0, n, m, [])
