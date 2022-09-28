import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    cmd = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    q = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if not len(q[0]):
        q.pop()
    rv = 0

    for i in cmd:
        if i == 'R':
            rv += 1
        else:
            if rv % 2:
                try:
                    q.pop()
                except:
                    print('error')
                    break
            else:
                try:
                    q.popleft()
                except:
                    print('error')
                    break
    else:
        if rv % 2:
            q.reverse()
            print('[', end='')
            for i in range(len(q)):
                if i < len(q) - 1:
                    print(f'{int(q[i])},', end='')
                else:
                    print(f'{int(q[i])}', end='')
            print(']')
        else:
            print('[', end='')
            for i in range(len(q)):
                if i < len(q) - 1:
                    print(f'{int(q[i])},', end='')
                else:
                    print(f'{int(q[i])}', end='')
            print(']')
