import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = dict()
for i in range(1, n + 1):
    dic[i] = sys.stdin.readline().rstrip()
dic_rv = dict(map(reversed,dic.items()))

for _ in range(m):
    search = sys.stdin.readline().rstrip()
    try:
        print(dic.get(int(search)))
    except:
        print(dic_rv.get(search))
        