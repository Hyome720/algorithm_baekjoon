import math

t = int(input())

for _ in range(t):
    n = int(input())
    is_false = 0
    if n == 4:
        print(2, 2)
    elif n == 6:
        print(3, 3)
    elif n == 8:
        print(3, 5)
    else:
        for num in range(n // 2, 1, -1):
            if is_false:
                break
            oppo = n - num
            for i in range(2, math.ceil(num ** (1 / 2)) + 1):
                if is_false:
                    break
                if num % i == 0:
                    break
            else:
                for i in range(2, math.ceil(oppo ** (1 / 2)) + 1):
                    if oppo % i == 0:
                        break
                else:
                    print(num, oppo)
                    is_false = 1
