n = int(input())
n_ori = n
n_copy = 0
cnt = 0

if n:
    while n_ori != n_copy:
        n = n % 10 * 10 + (n // 10 + n % 10) % 10
        n_copy = n
        cnt += 1
    print(cnt)
else:
    print(1)