import sys
import heapq

n = int(sys.stdin.readline().rstrip())

q = []
tmp = []
visited = [0] * n
is_full = [0] * n
check = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(q, (a, b))

while q:
    start_q, end_q = heapq.heappop(q)

    if not tmp:
        heapq.heappush(tmp, (end_q, 0))
        visited[0] += 1
        is_full[0] = 1
    else:
        while tmp:
            end_tmp, idx = heapq.heappop(tmp)
            if start_q > end_tmp:
                is_full[idx] = 0
            else:
                heapq.heappush(tmp, (end_tmp, idx))
                if len(tmp) == check + 1:
                    check += 1
                    heapq.heappush(tmp, (end_q, check))
                    is_full[check] = 1
                    visited[check] += 1
                    break
                else:
                    heapq.heappush(tmp, (end_q, is_full.index(0)))
                    visited[is_full.index(0)] += 1
                    is_full[is_full.index(0)] = 1
                    break
        else:
            heapq.heappush(tmp, (end_q, 0))
            visited[0] += 1
            is_full[0] = 1

if 0 in visited:
    cnt = visited.index(0)
    print(cnt)
    print(*visited[:cnt])
else:
    print(n)
    print(*visited)