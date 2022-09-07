word = list(input())
lst = [-1] * 26

for idx, value in enumerate(word):
    if lst[ord(value) - 97] == -1:
        lst[ord(value) - 97] = idx
print(*lst)