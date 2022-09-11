import sys


def is_palindrome(word, i):
    global cnt, res
    cnt += 1
    if i == mid:
        if word[i] == word[len(word) - 1 - i]:
            res = 1
            return res, cnt
        else:
            return res, cnt
    else:
        if word[i] == word[len(word) - 1 - i]:
            is_palindrome(word, i + 1)
            return res, cnt
        else:
            return res, cnt


n = int(input())

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    mid = len(word) // 2
    cnt = 0
    res = 0
    is_palindrome(word, 0)
    print(res, cnt)