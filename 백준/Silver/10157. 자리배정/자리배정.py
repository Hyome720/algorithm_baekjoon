w, h = map(int, input().split())
n = int(input())

# 좌석 사각형 위치 넣어줄 변수
p_num = 0
# 사각형의 시작점
start_num = 0
# 일단 설정
x, y = 1, 1
# 사각형 길이
x_leng, y_leng = 0, 0


# 제일 내부의 사각형의 크기 구하기
if w >= h:
    min_w = w - h
else:
    min_w = h - w

# 길이 리스트
i = 0
x_leng_lst = []
while w - i * 2 > 0:
    x_leng_lst.append(w - i * 2)
    i += 1

i = 0
y_leng_lst = []
while h - i * 2 > 0:
    y_leng_lst.append(h - i * 2)
    i += 1

# 만들어지는 사각형의 수, 인덱스로 써먹기 위해 1 빼줬음
sqr_num_idx = min(len(x_leng_lst), len(y_leng_lst)) - 1

min_x = x_leng_lst[sqr_num_idx]
min_y = y_leng_lst[sqr_num_idx]
min_sqr = min_x * min_y

sqr_lst = [min_sqr]

# 둘레의 수가 하나씩 증가할 때마다 8씩 증가
while sum(sqr_lst) < w * h:
    if len(sqr_lst) == 1 and (min_x == 1 or min_y == 1):
        min_sqr = min_sqr * 2 + 6
        sqr_lst.append(min_sqr)
    else:
        min_sqr += 8
        sqr_lst.append(min_sqr)


# 바깥 사각형부터 표기
sqr_lst.reverse()

# 사각형의 크기보다 n이 크다면 0 출력
if n > w * h:
    print(0)
# 몇 번째 사각형에 있는지 찾기
else:
    for i in range(len(sqr_lst)):
        if sum(sqr_lst[:i + 1]) >= n:
            p_num = i
            # 사각형의 시작 번호
            if p_num == 0:
                start_num = 1
            else:
                start_num = sum(sqr_lst[:p_num]) + 1
            x, y = p_num + 1, p_num + 1
            x_leng = x_leng_lst[p_num]
            y_leng = y_leng_lst[p_num]
            while start_num < n:
                if y_leng == 1:
                    x += n - start_num
                    start_num = n
                if x_leng == 1:
                    y += n - start_num
                    start_num = n
                if n - start_num > y_leng - 1:
                    y += y_leng - 1
                    start_num += y_leng - 1
                else:
                    y += n - start_num
                    start_num = n
                if n - start_num > 0:
                    if n - start_num < x_leng - 1:
                        x += n - start_num
                        start_num = n
                    else:
                        x += x_leng - 1
                        start_num += x_leng - 1
                if n - start_num > 0:
                    if n - start_num < y_leng - 1:
                        y -= n - start_num
                        start_num = n
                    else:
                        y -= y_leng - 1
                        start_num += y_leng - 1
                if n - start_num > 0:
                    x -= n - start_num
                    start_num = n
            print(x, y)
            break