import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
erase = int(sys.stdin.readline().rstrip())
visited = [-1] * n

tree = {}
tree_rv = {}
leaf = []

for idx, value in enumerate(lst):
    if tree.get(value):
        tree[value].append(idx)
    else:
        if value >= 0:
            tree[value] = [idx]
        else:
            root = idx

for idx, value in enumerate(lst):
    tree_rv[idx] = value

if erase != root:
    q_del = deque()
    q_del.append(erase)

    def dlt():
        while q_del:
            now = q_del.popleft()
            if tree.get(now):
                for nxt in tree[now]:
                    q_del.append(nxt)
                    if nxt == erase:
                        tree[now].remove(nxt)
                else:
                    del tree[now]

    dlt()

    tree[tree_rv[erase]].remove(erase)
    if not tree[tree_rv[erase]]:
        del tree[tree_rv[erase]]

    q = deque()
    q.append(root)

    def bfs():
        while q:
            now = q.popleft()
            if tree.get(now):
                for nxt in tree[now]:
                    q.append(nxt)
                    visited[nxt] = now
            else:
                leaf.append(now)

    bfs()
    print(len(leaf))
else:
    print(0)