n = int(input())
lst = []
i = 2

if n == 1:
    pass
else:
    while True:
        if n / i == 1:
            print(i)
            break
        elif n % i == 0:
            n //= i
            print(i)
        else:
            i += 1