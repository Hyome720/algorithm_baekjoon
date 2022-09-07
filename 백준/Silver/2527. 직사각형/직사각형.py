lst = list(list(map(int, input().split())) for _ in range(4))

for i in range(4):
    sqr_a = lst[i][:4]
    sqr_b = lst[i][4:]

    a_x = [sqr_a[0], sqr_a[2]]
    a_y = [sqr_a[1], sqr_a[3]]

    b_x = [sqr_b[0], sqr_b[2]]
    b_y = [sqr_b[1], sqr_b[3]]

    if a_x[1] < b_x[0] or b_x[1] < a_x[0] or a_y[1] < b_y[0] or b_y[1] < a_y[0]:
        print('d')
    elif a_x[1] == b_x[0] or b_x[1] == a_x[0]:
        if a_y[1] == b_y[0] or b_y[1] == a_y[0]:
            print('c')
        else:
            print('b')
    else:
        if a_y[1] == b_y[0] or b_y[1] == a_y[0]:
            print('b')
        else:
            print('a')