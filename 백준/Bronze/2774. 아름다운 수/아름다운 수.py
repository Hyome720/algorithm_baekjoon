n = int(input())
for _ in range(n):
    num = list(input())
    res = set()
    for i in num:
        res.add(i)
    print(len(res))