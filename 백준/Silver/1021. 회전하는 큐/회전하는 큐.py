from collections import deque

n, m = map(int, input().split())
lst = list(range(1, n + 1))
q = deque(lst)
find_lst = list(map(int, input().split()))
cnt = 0


for find in find_lst:
    lst = list(q)
    while lst[0] != find:
        if lst.index(find) <= len(lst) // 2:
            q.append(q.popleft())
            cnt += 1
        else:
            q.appendleft(q.pop())
            cnt += 1
        lst = list(q)
    q.popleft()

print(cnt)

