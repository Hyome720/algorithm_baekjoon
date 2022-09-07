from collections import deque

m, n = map(int, input().split())
lst = [[1] * m for _ in range(m)]
days = list(list(map(int, input().split())) for _ in range(n))

q = deque()

for day in days:
    for i in range(day[0]):
        q.append(0)
    for i in range(day[1]):
        q.append(1)
    for i in range(day[2]):
        q.append(2)
    i = 0
    j = 0

    while q:
        if m - 1 - i >= 0:
            lst[m - 1 - i][0] += q.popleft()
            i += 1
        else:
            lst[0][1 + j] += q.popleft()
            j += 1

for i in range(1, m):
    for j in range(1, m):
        if i >= j:
            lst[i][j] = max(lst[i][0], lst[0][j], lst[i - j][0])
        else:
            lst[i][j] = max(lst[i][0], lst[0][j], lst[0][j - i])

for i in lst:
    for j in i:
        print(j, end=" ")
    print()