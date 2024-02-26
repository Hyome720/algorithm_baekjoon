def solution(board, h, w):
    size = len(board)
    basic_color = board[h][w]
    cnt = 0
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    
    for i in range(0, 4):
        if 0 <= w + dx[i] < size and w != w + dx[i]:
            if board[h][w + dx[i]] == basic_color:
                cnt += 1
                
    for i in range(0, 4):
        if 0 <= h + dy[i] < size and h != h + dy[i]:
            if board[h + dy[i]][w] == basic_color:
                cnt += 1
    return cnt