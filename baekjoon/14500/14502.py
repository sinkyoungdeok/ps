from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())

board = []
wall = []

for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        if board[i][j] == 0:
            wall.append((i,j))

def diffusion(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                dfs(board, i, j)
    return

def dfs(board, ci, cj):
    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    for d in range(4):
        ni, nj = ci+di[d], cj+dj[d]
        if not(0 <= ni < N and 0 <= nj < M): continue
        if board[ni][nj] != 0 : continue
        board[ni][nj] = -1
        dfs(board, ni, nj)




    return

def count(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt +=1
    return cnt

res = 0

for c in combinations(wall, 3):
    # 벽 설치
    for x,y in c:
        board[x][y] = 1

    temp = deepcopy(board)
    diffusion(temp)
    res = max(res, count(temp))

    # 벽 초기화
    for x,y in c:
        board[x][y] = 0

print(res)





