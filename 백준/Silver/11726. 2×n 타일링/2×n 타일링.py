import sys

n = int(sys.stdin.readline().rstrip())

if n == 1:
    print(1)
else:
    lst = [1, 2] + [0] * (n - 2)
    t = 2
    while t < n:
        lst[t] = lst[t - 1] + lst[t - 2]
        t += 1
    
    print(lst[-1] % 10007)