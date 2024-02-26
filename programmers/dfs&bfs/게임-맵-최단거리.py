di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

from collections import deque

def bfs(maps, ci, cj, n, m):
    q = deque()
    q.append((0,0))
    
    while q:
        ci, cj= q.popleft()
        
        for d in range(4):
            ni, nj = di[d] + ci, dj[d] + cj
        
            if not (0 <= ni < n and 0 <= nj < m):
                continue

            if maps[ni][nj] == 0 or maps[ni][nj] > 1:
                continue
                
            maps[ni][nj] = maps[ci][cj] + 1
            q.append((ni, nj))
    
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]
    

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs(maps, 0, 0, n, m)
    return answer