import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)