n = int(input())
lst = list(map(int, input().split()))
max_score = max(lst)
new_sum = 0

for i in lst:
    new_sum += i / max_score * 100

print(new_sum / n)