a = int(input())
b = int(input())
c = b % 10
d = (b - c) % 100
e = b - c - d

print(a * c)
print(a * d // 10)
print(a * e // 100)
print(a * b)