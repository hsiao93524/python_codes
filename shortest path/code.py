H, W = list(map(int, input().split(" ")))
board = []
step = [(-1, 1), (-1, 0), (-1, -1)]
ori = []
max_board = dict()
for i in range(0, H):
    board.insert(0, list(map(int, input().split(" "))))
for j in range(0, W):
    max_board[(0, j)] = board[0][j]
for i in range(1, H):
    for j in range(0, W):
        max_val = -1
        for s in step:
            pos_h = i + s[0]
            pos_w = j + s[1]
            if pos_h >= H or pos_h < 0:
                continue
            if pos_w >= W or pos_w < 0:
                continue
            # print(max_board[(pos_h, pos_w)],  board[i][j])
            if max_val < max_board[(pos_h, pos_w)] + board[i][j]:
                max_val = max_board[(pos_h, pos_w)] + board[i][j]
        max_board[(i, j)] = max_val
        # print((i, j), max_val)
        
        
print(max(max_board.values()))
# print(max_board)