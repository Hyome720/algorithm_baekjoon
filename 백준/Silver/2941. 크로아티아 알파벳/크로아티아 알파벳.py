lst = list(input())

cnt = 0
i = 0

while i < len(lst):
    if i < len(lst) - 1:
        if lst[i] == 'c' and (lst[i + 1] == '-' or lst[i + 1] == '='):
            cnt += 1
            i += 2
        elif lst[i] == 'd' and lst[i + 1] == '-':
            cnt += 1
            i += 2
        elif lst[i] == 'l' and lst[i + 1] == 'j':
            cnt += 1
            i += 2
        elif lst[i] == 'n' and lst[i + 1] == 'j':
            cnt += 1
            i += 2
        elif lst[i] == 's' and lst[i + 1] == '=':
            cnt += 1
            i += 2
        elif lst[i] == 'z' and lst[i + 1] == '=':
            cnt += 1
            i += 2
        elif i < len(lst) - 2:
            if lst[i] == 'd' and lst[i + 1] == 'z' and lst[i + 2] == '=':
                cnt += 1
                i += 3
            else:
                cnt += 1
                i += 1
        else:
            cnt += 1
            i += 1
    else:
        cnt += 1
        i += 1

print(cnt)