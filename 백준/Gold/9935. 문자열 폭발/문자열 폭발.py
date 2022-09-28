import sys

word = list(sys.stdin.readline().rstrip())
bomb = sys.stdin.readline().rstrip()
bomb_cnt = len(bomb)

stack = []
cnt = 0

for i in word:
    stack.append(i)
    cnt += 1
    if cnt >= len(bomb):
        if "".join(stack[-bomb_cnt:]) == bomb:
            for _ in range(bomb_cnt):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print('FRULA')

