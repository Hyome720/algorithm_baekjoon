import sys


def factorial(n):
    memo = [1]
    cnt = 0
    for i in range(2, n + 1):
        memo.append(memo[-1] * i)
    for i in range(len(str(memo[-1])) - 1, -1, -1):
        if str(memo[-1])[i] == '0':
            cnt += 1
        else:
            break
    return cnt

n = int(input())
factorial(n)

print(factorial(n))