from collections import deque

M, N = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i,j,1))

di = [0,0,1,-1]
dj = [1,-1,0,0]

res = 1

while q:
    ci, cj, cnt = q.popleft()
    
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < N and 0 <= nj < M):
            continue
        
        if board[ni][nj] == -1 or board[ni][nj] > 0 :
            continue
        
        q.append((ni,nj,cnt+1))
        board[ni][nj] = cnt + 1
        res = cnt + 1
    

check = True
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            check = False 

if check:
    print(res-1)
else:
    print(-1)
    