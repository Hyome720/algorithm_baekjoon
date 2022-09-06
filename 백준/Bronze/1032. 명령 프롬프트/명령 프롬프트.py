n = int(input())

lst = list(input() for _ in range(n))
length = len(lst[0])
prompt = ''


for i in range(length):
    for j in range(1, n):
        if lst[0][i] != lst[j][i]:
            prompt += '?'
            break
    else:
        prompt += lst[0][i]

print(prompt)