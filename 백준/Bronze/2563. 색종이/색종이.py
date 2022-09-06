papers = int(input())
whitePaper = [[0] * 100 for _ in range(100)]

for _ in range(papers):
    X, Y = map(int, input().split())
    for i in range(Y, Y+10):         # 여기를 바로 whitePaper[i][Y:Y+10] 이런느낌으로... 굿
        for j in range(X, X+10):
            whitePaper[i][j] = 1

area = 0
for i in range(100):
    area += sum(whitePaper[i])
print(area)