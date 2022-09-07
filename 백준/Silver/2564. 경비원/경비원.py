w, h = map(int, input().split())
n = int(input())
store_lst = list(list(map(int, input().split())) for _ in range(n))
d_s, d_witch = list(map(int, input().split()))

# 최소거리들의 합
dist_sum = 0

if d_s == 1:
    for store in store_lst:
        if store[0] == 1:
            dist_sum += abs(store[1] - d_witch)
        elif store[0] == 2:
            dist_sum += h + min((store[1] + d_witch), (w * 2 - store[1] - d_witch))
        elif store[0] == 3:
            dist_sum += store[1] + d_witch
        elif store[0] == 4:
            dist_sum += store[1] + w - d_witch
elif d_s == 2:
    for store in store_lst:
        if store[0] == 1:
            dist_sum += h + min((store[1] + d_witch), (w * 2 - store[1] - d_witch))
        elif store[0] == 2:
            dist_sum += abs(store[1] - d_witch)
        elif store[0] == 3:
            dist_sum += h - store[1] + d_witch
        elif store[0] == 4:
            dist_sum += h - store[1] + w - d_witch
elif d_s == 3:
    for store in store_lst:
        if store[0] == 1:
            dist_sum += d_witch + store[1]
        elif store[0] == 2:
            dist_sum += h - d_witch + store[1]
        elif store[0] == 3:
            dist_sum += abs(store[1] - d_witch)
        elif store[0] == 4:
            dist_sum += w + min((store[1] + d_witch), (h * 2 - store[1] - d_witch))
else:
    for store in store_lst:
        if store[0] == 1:
            dist_sum += w - store[1] + d_witch
        elif store[0] == 2:
            dist_sum += w - store[1] + h - d_witch
        elif store[0] == 3:
            dist_sum += w + min((store[1] + d_witch), (h * 2 - store[1] - d_witch))
        elif store[0] == 4:
            dist_sum += abs(store[1] - d_witch)


print(dist_sum)