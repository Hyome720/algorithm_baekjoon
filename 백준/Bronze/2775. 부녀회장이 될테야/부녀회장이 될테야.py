def bunyeo(k, n):
    memo = [list(range(n + 1))] + [[0] * (n + 1) for _ in range(k)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for l in range(j + 1):
                memo[i][j] += memo[i - 1][l]
    # k층의 인덱스는 k + 1, n호는 그냥 n으로 하자
    return memo[k][n]


t = int(input())

for _ in range(t):
    # k층, n호
    k = int(input())
    n = int(input())

    print(bunyeo(k, n))