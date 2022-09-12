import sys

n, m = map(int, input().split())
name = set([sys.stdin.readline().rstrip() for _ in range(n)])
cnt = 0
noname = dict()

for i in range(m):
    someone = sys.stdin.readline().rstrip()
    if someone in name:
        noname[i] = someone
        cnt += 1

noname_sort = sorted(noname.items(), key=lambda x:x[1])

print(cnt)
for i in noname_sort:
    print(i[1])