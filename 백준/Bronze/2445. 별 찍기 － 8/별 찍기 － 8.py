import sys

n = int(input())
blank = ' '
star = '*'

for i in range(1, n + 1):
    print(f'{star * i}{blank * (n - i)}{blank * (n - i)}{star * i}')

for i in range(n - 1, 0, -1):
    print(f'{star * i}{blank * (n - i)}{blank * (n - i)}{star * i}')