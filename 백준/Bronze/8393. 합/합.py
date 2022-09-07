n = int(input())
n_sum = 0
if n % 2:
    n_sum = (n + 1) * (n // 2) + n // 2 + 1
else:
    n_sum = (n + 1) * (n // 2)

print(n_sum)