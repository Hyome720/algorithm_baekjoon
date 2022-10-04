import sys

n = int(sys.stdin.readline().rstrip())
lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))

total_minus = 0
total_zero = 0
total_one = 0


def paper(x, y, n):
    global total_minus, total_zero, total_one

    num_check = lst[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (lst[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        paper(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if num_check == -1:
        total_minus += 1
    elif num_check == 1:
        total_one += 1
    else:
        total_zero += 1

paper(0, 0, n)
print(total_minus)
print(total_zero)
print(total_one)
