import math

m = int(input())
n = int(input())
lst = []


for num in range(m, n + 1):
    if num == 1:
        pass
    elif num == 2:
        lst.append(num)
    else:
        for i in range(2, math.ceil(num ** (1 / 2)) + 1):
            if num % i == 0:
                break
                pass
        else:
            lst.append(num)

if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)