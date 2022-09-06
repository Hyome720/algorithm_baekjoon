import copy


# 주사위 갯수 받기
n = int(input())

lst = list(list(map(int, input().split())) for _ in range(n))
dice_lst = copy.deepcopy(lst)
tmp = 0
max_sum = []

for i in range(6):
    dice_lst = copy.deepcopy(lst)
    up = dice_lst[0][i]
    max_num = []
    for dice in dice_lst:
        idx = dice.index(up)
        down = up
        if idx == 0 or idx == 5:
            up = dice[5 - idx]
            del dice[5 - idx]
        elif idx == 1 or idx == 3:
            up = dice[4 - idx]
            del dice[4 - idx]
        else:
            up = dice[6 - idx]
            del dice[6 - idx]
        dice.remove(down)
    for dice in dice_lst:
        max_num.append(max(dice))
    max_sum.append(sum(max_num))

print(max(max_sum))