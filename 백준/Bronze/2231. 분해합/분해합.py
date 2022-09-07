n = int(input())
a = n - 1
res = n


while True:
    if n - a > 9 * len(str(n)):
        if res == n:
            res = 0
        break
    if n == a + a // 10 ** 6 % 10 + a // 10 ** 5 % 10 + a // 10 ** 4 % 10 + a // 10 ** 3 % 10 + a // 10 ** 2 % 10 + a // 10 % 10 + a % 10:
        res = a
        a -= 1
    else:
        a -= 1

print(res)