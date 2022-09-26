import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()
lst = list(word.strip('O'))
t = len(lst)

i = 0
cnt = 0

while i < t:
    long = 0
    if lst[i] == 'I':
        i += 1
        while i + 1 < t:
            if lst[i] == 'O' and lst[i + 1] == 'I':
                long += 1
                i += 2
            else:
                if long > n - 1:
                    cnt += long - n + 1
                break
        else:
            if long > n - 1:
                cnt += long - n + 1
            break
    else:
        i += 1

print(cnt)

