import sys

k, n = map(int, input().split())
lst = []

for _ in range(k):
    lst.append(int(sys.stdin.readline().rstrip()))

lan_sum = sum(lst)
size = lan_sum // n
langth = 1
lan_cnt = 0
max_langth = lan_sum // n
min_langth = 2

while True:
    lan_cnt = 0
    if max_langth - min_langth <= 1:
        break

    for i in lst:
        lan_cnt += i // langth
        if lan_cnt >= n:
            break

    if lan_cnt < n:
        max_langth = langth
        langth = (max_langth + min_langth) // 2
    else:
        min_langth = langth
        langth = (max_langth + min_langth) // 2

cnt_a = 0
cnt_b = 0

for i in lst:
    cnt_a += i // min_langth
    cnt_b += i // max_langth

if cnt_b >= n:
    print(max_langth)
else:
    print(min_langth)