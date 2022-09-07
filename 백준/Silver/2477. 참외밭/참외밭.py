melon = int(input())
area = list(list(map(int, input().split())) for _ in range(6))
total_area = 0
total_melon = 0

# 가장 큰 사각형 넓이 구하기
x = []
y = []

for a in area:
    if a[0] <= 2:
        x.append(a[1])
    else:
        y.append(a[1])
max_area = max(x) * max(y)

# 진행 방향 보기

heading = []

for a in area:
    heading.append(a[0])

# 세로 가장 긴변 보기
long = 0
idx = 0

for i in range(6):
    if area[i][0] >= 3:
        long = max(area[i][1], long)

# 거기 인덱스 찾기
for i in range(6):
    if area[i][0] >= 3:
        if area[i][1] == long:
            idx = i

# 가장 작은 사각형 찾기
small_x = 0
small_y = 0
min_area = 0

if sum(heading) % 2:
    small_x = area[(idx + 2) % 6][1]
    small_y = area[(idx + 3) % 6][1]
    min_area = small_x * small_y
else:
    small_x = area[(idx + 3) % 6][1]
    small_y = area[(idx + 4) % 6][1]
    min_area = small_x * small_y


total_area = max_area - min_area
total_melon = total_area * melon

print(total_melon)