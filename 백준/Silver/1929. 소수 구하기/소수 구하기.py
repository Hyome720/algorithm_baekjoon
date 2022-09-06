import math

m, n = map(int, input().split())


for num in range(m, n + 1):
    if num == 1:
        pass
    elif num == 2:
        print(num)
    else:
        for i in range(2, math.ceil(num ** (1 / 2)) + 1):
            if num % i == 0:
                break
                pass
        else:
            print(num)

