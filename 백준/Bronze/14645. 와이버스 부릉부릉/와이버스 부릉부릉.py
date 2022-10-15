import sys

while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if not a:
        print('비와이')
        break