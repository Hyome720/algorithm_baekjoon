n = int(input())
cnt = 0
for _ in range(n):
    lst = list(input())
    check_lst = []
    for i in lst:
        if i not in check_lst or check_lst[-1] == i:
            check_lst.append(i)
        else:
            break
    else:
        cnt += 1

print(cnt)