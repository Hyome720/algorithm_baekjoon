# 빙고 리스트
bingo = list(list(map(int, input().split())) for _ in range(5))
f_index = 0

# 완성된 빙고 수
cnt = 0

# 사회자가 부를 번호 담을 리스트
call = []

for _ in range(5):
    call.append(list(map(int, input().split())))

# 리스트 언패킹해서 1차원 리스트로 재배열
lst = []

for i in range(5):
    lst += [*call[i]]


def b_f(bingo, lst):
    for call_num in lst:
        cnt = 0
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == call_num:
                    bingo[i][j] = 0
        # if lst.index(call_num) >= 12:
        for k in range(5):
            if cnt >= 3:
                f_index = lst.index(call_num) + 1
                return f_index
            for l in range(5):
                if bingo[k][l] == 0:
                    pass
                else:
                    break
            else:
                cnt += 1
        for l in range(5):
            if cnt >= 3:
                f_index = lst.index(call_num) + 1
                return f_index
            for k in range(5):
                if bingo[k][l] == 0:
                    pass
                else:
                    break
            else:
                cnt += 1
        for l in range(5):
            if cnt >= 3:
                f_index = lst.index(call_num) + 1
                return f_index
            if bingo[l][l] == 0:
                pass
            else:
                break
        else:
            cnt += 1
        for l in range(5):
            if cnt >= 3:
                f_index = lst.index(call_num) + 1
                return f_index
            if bingo[4 - l][l] == 0:
                pass
            else:
                break
        else:
            cnt += 1
        if cnt >= 3:
            f_index = lst.index(call_num) + 1
            return f_index


print(b_f(bingo, lst))