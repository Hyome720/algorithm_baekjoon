def switch(sex, switch_num):
    i = 1
    if sex == 1:
        while switch_num * i - 1 < n:
            if switches[switch_num * i - 1]:
                switches[switch_num * i - 1] = 0
            else:
                switches[switch_num * i - 1] = 1
            i += 1
    else:
        if switches[switch_num - 1]:
            switches[switch_num - 1] = 0
        else:
            switches[switch_num - 1] = 1
        while switch_num - 1 - i >= 0 and switch_num - 1 + i < n and switches[switch_num - 1 - i] == switches[switch_num - 1 + i]:
            if switches[switch_num - 1 - i]:
                switches[switch_num - 1 - i] = 0
                switches[switch_num - 1 + i] = 0
            else:
                switches[switch_num - 1 - i] = 1
                switches[switch_num - 1 + i] = 1
            i += 1
    return switches


n = int(input())
switches = list(map(int, input().split()))
stu_nums = int(input())

for _ in range(stu_nums):
    sex, switch_num = map(int, input().split())
    switch(sex, switch_num)

for i in range(0, n, 20):
    print(*switches[i:i+20])