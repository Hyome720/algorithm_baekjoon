import sys
import heapq

q = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    if t:
        if t > 0:
            heapq.heappush(q, (t, 1))
        else:
            heapq.heappush(q, (-t, -1))
    else:
        if q:
            num, plus = heapq.heappop(q)
            print(num * plus)
        else:
            print(0)