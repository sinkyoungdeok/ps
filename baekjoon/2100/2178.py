"""
문제 링크: https://www.acmicpc.net/problem/2178
문제 접근 방법: bfs
"""

from collections import deque 

N, M = map(int, input().split())

miro = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    miro.append(list(input()))

q = deque()
q.append((0,0,1))
miro[0][0] = 0


while q:
    curr = q.popleft()
    cx, cy, cnt = curr[0], curr[1], curr[2]

    if cx == N-1 and cy == M-1:
        print(cnt)
        break
    
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == '1':
            q.append((nx,ny,cnt+1))
            miro[nx][ny] = 0
        
