n = int(input())
a = ' '
b = '*'

for i in range(1, n + 1):
    print(f'{a * (n - i)}{b * i}')