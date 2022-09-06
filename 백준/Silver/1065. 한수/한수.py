
def hansoo(n):
    global cnt
    if n < 10:
        cnt = n
        return cnt
    else:
        for i in range(1, n + 1):
            if i < 10:
                cnt += 1
            else:
                num = str(i)
                gap = int(num[0]) - int(num[1])
                for j in range(len(num) - 1):
                    diff = int(num[j]) - int(num[j + 1])
                    if gap != diff:
                        break
                else:
                    cnt += 1
        return cnt


cnt = 0
n = int(input())
hansoo(n)

print(cnt)