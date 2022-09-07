n = int(input())
dist = 0
if n == 1:
    print(1)
else:
    while True:
        if 6 * ((dist + 1) * dist / 2) + 2 <= n < 6 * ((dist + 2) * (dist + 1) / 2) + 2:
            break
        else:
            dist += 1
    print(dist + 2)