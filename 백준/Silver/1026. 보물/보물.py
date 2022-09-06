n = int(input())

lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))
min_sum = 0

for _ in range(n):
    min_sum += lst_a.pop(lst_a.index(min(lst_a))) * lst_b.pop(lst_b.index(max(lst_b)))

print(min_sum)