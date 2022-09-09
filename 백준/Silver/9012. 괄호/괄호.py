import sys

k = int(input())

for _ in range(k):
    lst = []
    vps = sys.stdin.readline()
    for i in vps:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if lst:
                if lst[-1] == '(':
                    lst.pop()
            else:
                print('NO')
                break
    else:
        if lst:
            print('NO')
        else:
            print('YES')