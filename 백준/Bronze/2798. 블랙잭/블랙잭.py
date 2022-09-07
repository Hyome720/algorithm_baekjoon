n, m = map(int, input().split())
lst = list(map(int, input().split()))
tmp_sum = m + 1

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if m < lst[i] + lst[j] + lst[k]:
                continue
            else:
                if m - (lst[i] + lst[j] + lst[k]) < tmp_sum:
                    tmp_sum = m - (lst[i] + lst[j] + lst[k])

print(m - tmp_sum)