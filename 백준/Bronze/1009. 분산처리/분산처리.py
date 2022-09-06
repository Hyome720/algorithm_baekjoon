n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if a % 10 == 1:
        print(1)
    if a % 10 == 2:
        if b % 4 == 1:
            print(2)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(8)
        else:
            print(6)
    if a % 10 == 3:
        if b % 4 == 1:
            print(3)
        elif b % 4 == 2:
            print(9)
        elif b % 4 == 3:
            print(7)
        else:
            print(1)
    if a % 10 == 4:
        if b % 2 == 1:
            print(4)
        else:
            print(6)
    if a % 10 == 5:
        print(5)
    if a % 10 == 6:
        print(6)
    if a % 10 == 7:
        if b % 4 == 1:
            print(7)
        elif b % 4 == 2:
            print(9)
        elif b % 4 == 3:
            print(3)
        else:
            print(1)
    if a % 10 == 8:
        if b % 4 == 1:
            print(8)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(2)
        else:
            print(6)
    if a % 10 == 9:
        if b % 2 == 1:
            print(9)
        else:
            print(1)
    if a % 10 == 0:
        print(10)
