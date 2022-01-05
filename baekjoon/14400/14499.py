N, M, x, y, K = map(int, input().split())

left, right, up, down, forward, backword = 0,0,0,0,0,0

board = []
for i in range(N):
    board.append( list(map(int, input().split()))) 
for i in map(int,input().split()):
    if i == 1: # 동쪽
        if y + 1 == M:
            continue
        temp = down
        down = right
        right = up
        up = left
        left = temp
        y+=1
        if board[x][y]:
            down = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = down
        print(up)
    elif i == 2: # 서쪽
        if y - 1 == -1:
            continue
        temp = down
        down = left
        left = up
        up = right
        right = temp
        y -= 1
        if board[x][y]:
            down = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = down
        print(up)
    elif i == 3: # 북쪽
        if x - 1 == -1:
            continue
        temp = down
        down = backword
        backword = up
        up = forward
        forward = temp
        x -= 1
        if board[x][y]:
            down = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = down
        print(up)
    elif i == 4: # 동쪽 
        if x + 1 == N:
            continue
        temp = down
        down = forward
        forward = up
        up = backword
        backword = temp
        x += 1
        if board[x][y]:
            down = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = down
        print(up)