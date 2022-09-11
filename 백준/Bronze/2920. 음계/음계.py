import sys

lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst_as = sorted(lst)
lst_ds = sorted(lst, reverse=True)

if lst == lst_ds:
    print('descending')
elif lst == lst_as:
    print('ascending')
else:
    print('mixed')