c = int(input())
for _ in range(c):
    lst = list(map(int, input().split()))
    score_sum = 0
    cnt = 0

    for i in range(1, lst[0] + 1):
        score_sum += lst[i]
    avg = score_sum / lst[0]

    for i in range(1, lst[0] + 1):
        if lst[i] > avg:
            cnt += 1

    percent = cnt / (len(lst) - 1) * 100

    print("{:.3f}".format(percent) + '%')