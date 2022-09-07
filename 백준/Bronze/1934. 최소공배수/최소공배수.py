def hose(a, b):
    global max_num
    global nam_num
    if a < b:
        a, b = b, a
    if a % b == 0:
        max_num = b
        return max_num
    else:
        nam_num = a % b
        a = b
        b = nam_num
        hose(a, b)


t = int(input())
for case in range(t):
    a, b = map(int, input().split())
    gop = a * b
    max_num = 0
    nam_num = 0
    hose(a, b)
    print(gop // max_num)