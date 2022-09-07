t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h:
        end_num = n // h + 1
        order = (end_num - 1) * h + 1
        start = n - order + 1
        room = start * 100
        print(room + end_num)
    else:
        end_num = n // h
        order = (end_num - 1) * h + 1
        start = n - order + 1
        room = start * 100
        print(room + end_num)