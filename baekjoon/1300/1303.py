"""
문제 링크: https://www.acmicpc.net/problem/1303
문제 접근 방법: bfs + 브루트포스
"""
from collections import deque 
N, M = map(int, input().split())
board = []
for i in range(M):
    board.append(list(input()))

q = deque()
W = 0
B = 0

di = [0,0,1,-1]
dj = [1,-1,0,0]



for i in range(M):
    for j in range(N):
        if board[i][j] == "0":
            continue
        wb_temp = board[i][j]
        q.append((i,j))
        board[i][j] = "0"
        
        count = 0
        while q:
            curr = q.popleft()
            ci, cj = curr[0], curr[1]
            count +=1

            for d in range(4):
                ni = ci + di[d]
                nj = cj + dj[d]

                if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == wb_temp :
                    q.append((ni,nj))
                    board[ni][nj] = "0"
        
        count = count * count

        if wb_temp == "W":
            W += count
        if wb_temp == "B":
            B += count

print(W,B)
            
