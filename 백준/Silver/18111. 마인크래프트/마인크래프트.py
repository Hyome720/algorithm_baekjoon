import sys
from copy import deepcopy

def best(block, k):
    block_copy = deepcopy(block)
    b_copy = b
    time = 0

    for i in range(len(block_copy)):
        if block_copy[i][0] > k:
            time += (block_copy[i][0] - k) * 2 * block_copy[i][1]
            b_copy += (block_copy[i][0] - k) * block_copy[i][1]
        else:
            time += (k - block_copy[i][0]) * block_copy[i][1]
            b_copy -= (k - block_copy[i][0]) * block_copy[i][1]
    else:
        if b_copy < 0:
            return
        else:
            ans_lst.append([time, k])
            return ans_lst


n, m, b = map(int, sys.stdin.readline().rstrip().split())
lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
block = dict()
ans_lst = []

for i in range(n):
    for j in range(m):
        if block.get(lst[i][j]):
            block[lst[i][j]] += 1
        else:
            block[lst[i][j]] = 1

test = deepcopy(block)
block = sorted(block.items(), key=lambda x:(x[1], x[0]))
max_len = len(block)
block_search = sorted(test.items(), key=lambda x:(x[0]))
ground_lst = list(i for i in range(block_search[0][0], block_search[-1][0] + 1))

for k in ground_lst:
    best(block, k)

ans_dic = dict()

for i in range(len(ans_lst)):
    ans_dic[i] = ans_lst[i]

ans_dic = sorted(ans_dic.items(), key=lambda x:(-x[1][0], x[1][1]))
print(*ans_dic[-1][1])