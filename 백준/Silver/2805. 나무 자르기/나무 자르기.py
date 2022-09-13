import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

max_h = max(lst)
min_h = 0

while min_h <= max_h:
    h = (max_h + min_h) // 2
    tree_sum = 0

    for i in lst:
        if i - h > 0:
            tree_sum += i - h

    if tree_sum < m:
        max_h = h - 1
    else:
        min_h = h + 1

print(max_h)