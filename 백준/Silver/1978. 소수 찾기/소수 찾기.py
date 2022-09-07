import math


# 주사위 갯수 받기
n = int(input())
lst = list(map(int, input().split()))
cnt = 0

for num in lst:
    if num == 1:
        pass
    elif num == 2:
        cnt += 1
    else:
        for i in range(2, math.ceil(num ** (1 / 2)) + 1):
            if num % i == 0:
                break
                pass
        else:
            cnt += 1

print(cnt)