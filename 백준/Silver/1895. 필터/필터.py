import statistics

r, c = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(r))
t = int(input())
filter_lst = []
cnt = 0

for i in range(r - 2):
    for j in range(c - 2):
        filter = []
        filter_num = 0
        for k in range(3):
            for l in range(3):
                filter.append(lst[i + k][j + l])
        else:
            filter_num = statistics.median(filter)
            filter_lst.append(filter_num)

for i in filter_lst:
    if i >= t:
        cnt += 1

print(cnt)