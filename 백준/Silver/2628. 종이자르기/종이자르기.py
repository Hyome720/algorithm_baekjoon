w, h = map(int, input().split())
n = int(input())
cut_lst = list(list(map(int, input().split())) for _ in range(n))

# 가로 세로 분류
w_cut_lst = []
h_cut_lst = []

for cut in cut_lst:
    if cut[0]:
        w_cut_lst.append(cut)
    else:
        h_cut_lst.append(cut)

# 가로 세로에서 자를 값만 출력
w_cut = [0, w]
h_cut = [0, h]

for cut in w_cut_lst:
    w_cut.append(cut[1])
for cut in h_cut_lst:
    h_cut.append(cut[1])

w_cut.sort()
h_cut.sort()

# 자를 길이들 출력
w_size = []
h_size = []

for i in range(len(w_cut) - 1):
    w_size.append(w_cut[i + 1] - w_cut[i])
for i in range(len(h_cut) - 1):
    h_size.append(h_cut[i + 1] - h_cut[i])

print(max(w_size) * max(h_size))