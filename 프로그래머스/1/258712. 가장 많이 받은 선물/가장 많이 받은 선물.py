def solution(friends, gifts):
    gift_table = dict()
    max_result = 0
    tmp_result = 0
    for i in friends:
        gift_table[i] = {'idx' : 0}
        for j in friends:
            if i == j:
                pass
            else:
                gift_table[i][j] = 0

    for i in gifts:
        cnt = i.split(' ')
        gift_table[cnt[0]]['idx'] += 1
        gift_table[cnt[1]]['idx'] -= 1
        gift_table[cnt[0]][cnt[1]] -= 1
        gift_table[cnt[1]][cnt[0]] += 1

    for i in gift_table:
        tmp_result = 0
        for j in gift_table[i]:
            if j == 'idx':
                pass
            else:
                if gift_table[i][j] < 0:
                    tmp_result += 1
                elif gift_table[i][j] == 0 and gift_table[i]['idx'] > gift_table[j]['idx']:
                    tmp_result += 1
        print(tmp_result)
        if tmp_result > max_result:
            max_result = tmp_result
                    
    return max_result