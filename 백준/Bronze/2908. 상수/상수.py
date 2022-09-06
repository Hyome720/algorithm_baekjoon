a, b = map(int, input().split())

hun_a = a // 100
hun_b = b // 100
one_a = a % 10
one_b = b % 10

a = a // 10 % 10 * 10 + hun_a + one_a * 100
b = b // 10 % 10 * 10 + hun_b + one_b * 100

print(max(a, b))