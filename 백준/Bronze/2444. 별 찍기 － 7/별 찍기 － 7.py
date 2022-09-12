import sys

n = int(input())
blank = ' '
star = '*'

for i in range(1, n):
    print(f'{blank * (n - i)}{star * (2 * i - 1)}')

for i in range(n, 0, -1):
    print(f'{blank * (n - i)}{star * (2 * i - 1)}')