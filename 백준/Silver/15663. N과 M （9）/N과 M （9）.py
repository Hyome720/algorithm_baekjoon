import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

lst.sort()

visited = [0] * n
temp = list()


def dfs():
    if len(temp) == m:
        print(*temp)
        return
    last = 0
    for i in range(n):
        if not visited[i] and last != lst[i]:
            visited[i] = 1
            temp.append(lst[i])
            last = lst[i]
            dfs()
            visited[i] = 0
            temp.pop()

dfs()

