import sys
from collections import Counter

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))

if -0.5 < round(sum(lst) / n) < 0:
    print(0)
else:
    print(round(sum(lst) / n))
lst.sort()
print(lst[len(lst) // 2])
if len(Counter(lst).most_common(2)) == 1:
    print(Counter(lst).most_common(2)[0][0])
elif len(Counter(lst).most_common(2)):
    if Counter(lst).most_common(2)[0][1] == Counter(lst).most_common(2)[1][1]:
        print(Counter(lst).most_common(2)[1][0])
    else:
        print(Counter(lst).most_common(2)[0][0])
print(lst[-1] - lst[0])
