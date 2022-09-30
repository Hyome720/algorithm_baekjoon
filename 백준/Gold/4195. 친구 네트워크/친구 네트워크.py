import sys

t = int(sys.stdin.readline().rstrip())
ans = []

def find(someone):
    if dic.get(someone):
        while someone != dic[someone][0]:
            someone = dic[dic[someone][0]][0]
    else:
        dic[someone] = [someone, 1, 1]
    return dic[someone][0]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return dic[x][1]
    elif dic[x][1] == dic[y][1]:
        dic[y][0] = dic[x][0]
        dic[x][2] += 1
        dic[x][1] += dic[y][1]
        return dic[x][1]
    elif dic[x][1] < dic[y][1]:
        dic[x][0] = dic[y][0]
        dic[y][1] += dic[x][1]
        return dic[y][1]
    else:
        dic[y][0] = dic[x][0]
        dic[x][1] += dic[y][1]
        return dic[x][1]

for _ in range(t):
    f = int(sys.stdin.readline().rstrip())
    dic = dict()
    for _ in range(f):
        a, b = sys.stdin.readline().rstrip().split()
        print(union(a, b))

