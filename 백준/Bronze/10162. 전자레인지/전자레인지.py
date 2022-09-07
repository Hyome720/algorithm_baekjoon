t = int(input())

lst = []
a = t // 300
b = (t - a * 300) // 60
c = (t - a * 300 - b * 60) // 10

if t == a * 300 + b * 60 + c * 10:
    print(a, b, c)
else:
    print(-1)