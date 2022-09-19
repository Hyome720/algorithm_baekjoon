import sys

word = list(sys.stdin.readline().rstrip())
q = int(sys.stdin.readline().rstrip())

lst = list([0] * len(word) for _ in range(26))
lst[ord(word[0]) - 97][0] = 1

for i in range(1, len(word)):
    for j in range(26):
        if j == ord(word[i]) - 97:
            lst[j][i] = lst[ord(word[i]) - 97][i - 1] + 1
        else:
            lst[j][i] = lst[j][i - 1]

for _ in range(q):
    a_i, l_i, r_i = sys.stdin.readline().rstrip().split()
    l_i = int(l_i)
    r_i = int(r_i)

    if l_i:
        res = lst[ord(a_i) - 97][r_i] - lst[ord(a_i) - 97][l_i - 1]
    else:
        res = lst[ord(a_i) - 97][r_i]

    print(res)
