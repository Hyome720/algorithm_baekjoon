import sys

total, tar = map(int, sys.stdin.readline().split())
tem = list(map(int, sys.stdin.readline().split()))

prepix = [0 for i in range(tar)]
presum = 0


prepix[0] = 1


for i in range(total):
    presum += tem[i]
    prepix[presum % tar] += 1

ans = 0
for i in prepix:
    ans += i * (i-1) // 2

print(ans)