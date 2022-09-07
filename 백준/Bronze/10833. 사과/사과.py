n = int(input())
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())
    cnt += b % a

print(cnt)