n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
better = []

for i in range(n):
    cnt = 1
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    else:
        better.append(cnt)

print(*better)