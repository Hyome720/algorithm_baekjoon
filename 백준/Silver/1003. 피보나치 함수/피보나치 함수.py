import sys

def fibonacci(n):
    global fibo
    fibo = [0, 1] #배열에 피보나치 수열 값을 순서대로 저장
    for i in range(2, n + 1): #n번째에 도달할 때까지 연산
        fibo.append(fibo[i-1] + fibo[i-2]) #i번째 수열을 계산하여 배열에 삽입
    return fibo[n]

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    fibonacci(n)


    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibo[-2], fibo[-1])