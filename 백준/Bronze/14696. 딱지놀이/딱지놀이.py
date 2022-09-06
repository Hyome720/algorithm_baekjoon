n = int(input())

for _ in range(n):
    a_case = list(map(int, input().split()))
    b_case = list(map(int, input().split()))

    a_num = a_case[0]
    a_scab = a_case[1:]
    a_scab.sort(reverse=True)

    b_num = b_case[0]
    b_scab = b_case[1:]
    b_scab.sort(reverse=True)

    fight = min(len(a_scab), len(b_scab))

    for i in range(fight):
        if a_scab[i] > b_scab[i]:
            print('A')
            break
        elif a_scab[i] < b_scab[i]:
            print('B')
            break
        else:
            pass
    else:
        if len(a_scab) > len(b_scab):
            print('A')
        elif len(a_scab) < len(b_scab):
            print('B')
        else:
            print('D')