while True:
    num = input()
    if num == '0':
        break
    check = len(num) // 2

    for i in range(check):
        if num[i] == num[len(num) - 1 - i]:
            pass
        else:
            print('no')
            break
    else:
        print('yes')