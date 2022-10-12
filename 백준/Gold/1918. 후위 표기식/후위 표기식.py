import sys

lst = list(sys.stdin.readline().rstrip())
stack = []
res = ''

for word in lst:
    if word.isalpha():
        res += word
    else:
        if word == '(':
            stack.append(word)
        elif word == '*' or word == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(word)
        elif word == '+' or word =='-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(word)
        else:
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)