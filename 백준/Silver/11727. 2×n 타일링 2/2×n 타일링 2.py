import sys

n = int(sys.stdin.readline().rstrip())

if n == 1:
    print(1)
else:
    lst = [1] + [0] * (n - 1)
    t = 1
    while t < n:
        if (t + 1) % 2:
            lst[t] = lst[t - 1] * 2 - 1
        else:
            lst[t] = lst[t - 1] * 2 + 1
        t += 1

    print(lst[-1] % 10007)