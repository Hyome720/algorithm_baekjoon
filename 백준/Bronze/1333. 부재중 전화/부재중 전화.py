n, l, d = map(int, input().split())

check = [0] * (n * l + 5 * (n - 1))

for i in range(n):
    s = (l + 5) * i
    for j in range(s, s + l):
        check[j] = 1

ans = 0
while ans < len(check):
    if not check[ans]:
        break
    ans += d
    
print(ans)
