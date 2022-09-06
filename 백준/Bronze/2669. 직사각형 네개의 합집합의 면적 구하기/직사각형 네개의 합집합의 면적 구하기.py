area = list(list([0] * 100) for _ in range(100))

for _ in range(4):
    x_s, y_s, x_e, y_e = map(int, input().split())
    for i in range(x_s, x_e):
        for j in range(y_s, y_e):
            area[i][j] = 1

area_sum = 0
for i in range(100):
    area_sum += sum(area[i])
print(area_sum)