import sys

n = int(input())
lst = []

for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))

    if cmd[0] == 'push':
        lst.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(lst))
    elif cmd[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    else:
        if lst:
            print(lst[-1])
        else:
            print(-1)