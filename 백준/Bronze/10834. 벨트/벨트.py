m = int(input())
lst = list(list(map(int, input().split())) for _ in range(m))

gop = 1
turn = 0

for belt in lst:
    turn += belt[2]

for i in range(m):
    gop *= lst[i][1] / lst[i][0]

print(turn % 2, int(gop))