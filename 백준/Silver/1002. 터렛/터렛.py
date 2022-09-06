n = int(input())

for _ in range(n):
    lst = list(map(int, input().split()))
    dist = (lst[3] - lst[0]) ** 2 + (lst[4] - lst[1]) ** 2
    diff = (lst[5] - lst[2]) ** 2
    plus = (lst[5] + lst[2]) ** 2

    if dist == 0 and diff == 0:
        print(-1)
    elif diff < dist < plus:
        print(2)
    elif dist == diff or dist == plus:
        print(1)
    else:
        print(0)