lst = list(list(map(int, input().split())) for _ in range(3))

x_lst = []
y_lst = []

for i in range(3):
    if lst[i][0] not in x_lst:
        x_lst.append(lst[i][0])
    else:
        x_lst.remove(lst[i][0])
    if lst[i][1] not in y_lst:
        y_lst.append(lst[i][1])
    else:
        y_lst.remove(lst[i][1])

print(*x_lst, *y_lst)