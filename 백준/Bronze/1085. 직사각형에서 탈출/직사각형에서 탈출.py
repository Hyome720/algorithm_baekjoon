x, y, w, h = map(int, input().split())
dist = min(abs(x - w), x, abs(y - h), y)

print(dist)
