lst = list(map(int, input().split()))
lst.sort()

dice = set(lst)
if len(dice) == 1:
    print(10000 + 1000 * lst[0])
elif len(dice) == 3:
    print(100 * lst[2])
else:
    print(1000 + 100 * lst[1])