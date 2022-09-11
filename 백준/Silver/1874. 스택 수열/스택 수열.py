import sys

n = int(sys.stdin.readline().rstrip())
lst = list(range(1, n + 1))
res = []
stack = []
is_false = 0

for _ in range(n):
    k = int(sys.stdin.readline().rstrip())
    while True:
        if stack:
            if stack[-1] == k:
                stack.pop()
                res.append('-')
                break
            else:
                try:
                    stack.append(lst[0])
                    lst.remove(lst[0])
                    res.append('+')
                except:
                    is_false = 1
                    break
        else:
            try:
                stack.append(lst[0])
                lst.remove(lst[0])
                res.append('+')
            except:
                is_false = 1
                break
    if is_false:
        break

if is_false:
    print('NO')
else:
    for i in res:
        print(i)