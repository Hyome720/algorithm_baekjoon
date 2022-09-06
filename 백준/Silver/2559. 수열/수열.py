n, k = map(int, input().split())
lst = list(map(int, input().split()))
temp_sums = sum(lst[0:k])
max_sum = sum(lst[0:k])

for i in range(len(lst) - k):
    temp_sums = temp_sums - lst[i] + lst[i + k]
    if temp_sums > max_sum:
        max_sum = temp_sums


print(max_sum)