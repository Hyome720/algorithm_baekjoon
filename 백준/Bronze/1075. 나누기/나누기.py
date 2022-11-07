import sys

num = int(sys.stdin.readline().rstrip())
f = int(sys.stdin.readline().rstrip())

res = num // 100 * 100 // f * f

if not res % f and res >= num // 100 * 100:
    n = list(str(num // 100 * 100 // f * f))
else:
    n = list(str(num // 100 * 100 // f * f + f))


print(n[-2] + n[-1])