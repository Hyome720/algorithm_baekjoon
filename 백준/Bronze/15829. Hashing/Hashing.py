import sys

l = int(input())
word = sys.stdin.readline().rstrip()
hashing = 0

for i in range(l):
    hashing += (ord(word[i]) - 96) * (31 ** i)

print(divmod(hashing, 1234567891)[1])