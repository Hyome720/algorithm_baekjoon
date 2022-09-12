import sys

n = int(input())
blank = ' '
star = '*'

for i in range(1, n + 1):
    print(f'{blank * (n - i)}{star * (2 * i - 1)}')