import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    word = list(sys.stdin.readline().rstrip())
    print(f'{word[0]}{word[-1]}')
