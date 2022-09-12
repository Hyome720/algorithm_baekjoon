import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort(reverse=True)
cnt = 0

for i in lst:
    cnt += k // i
    k %= i

print(cnt)