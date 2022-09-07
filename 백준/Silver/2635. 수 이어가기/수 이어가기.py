n = int(input())
max_cnt = 0
max_num = 0
i = 1

while i <= n:
    num_lst = [n, i]
    cnt = 2
    while num_lst[-2] - num_lst[-1] >= 0:
        num_lst.append(num_lst[-2] - num_lst[-1])
        cnt += 1
    if cnt > max_cnt:
        max_num = i
    max_cnt = max(max_cnt, cnt)
    i += 1

res = [n, max_num]
while res[-2] - res[-1] >= 0:
    res.append(res[-2] - res[-1])


print(max_cnt)
print(*res)