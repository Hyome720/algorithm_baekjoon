import sys

n = int(sys.stdin.readline().rstrip())
dic = dict()
for _ in range(n):
    member = sys.stdin.readline().rstrip()
    if dic.get(member[0]):
        dic[member[0]] += 1
    else:
        dic[member[0]] = 1

dic = sorted(dic.items(), key=lambda x: x[0])

ans = []
for i in dic:
    if i[1] >= 5:
        ans.append(i[0])

if ans:
    for i in ans:
        print(i, end='')
else:
    print('PREDAJA')
