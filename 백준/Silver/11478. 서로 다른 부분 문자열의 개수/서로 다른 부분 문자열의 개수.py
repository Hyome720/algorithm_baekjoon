import sys

word = sys.stdin.readline().rstrip()
res = set()

for i in range(len(word)):
    for j in range(i + 1, len(word) + 1):
        res.add(word[i:j])

print(len(res))
