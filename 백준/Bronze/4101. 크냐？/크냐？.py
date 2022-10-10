import sys

while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if not a:
        break
    if a > b:
        print('Yes')
    else:
        print('No')