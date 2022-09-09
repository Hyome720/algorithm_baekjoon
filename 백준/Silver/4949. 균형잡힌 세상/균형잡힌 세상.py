import sys

while True:
    lst = []
    vps = sys.stdin.readline().rstrip()
    if vps == '.':
        break
    for i in vps:
        if i == '.':
            break
        elif i == '(' or i == '[':
            lst.append(i)
        elif i == ')':
            if lst:
                if lst[-1] == '(':
                    lst.pop()
                else:
                    break
            else:
                lst.append(i)
                break
        elif i == ']':
            if lst:
                if lst[-1] == '[':
                    lst.pop()
                else:
                    break
            else:
                lst.append(i)
                break
    if lst:
        print('no')
    else:
        print('yes')
