n = int(input())

for case in range(1, n + 1):
    a, b = map(int, input().split())
    print(f'Case #{case}: {a} + {b} = {a + b}')