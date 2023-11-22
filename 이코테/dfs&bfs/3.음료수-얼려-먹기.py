"""
4 5
00110
00011
11111
00000

"""

N, M = map(int, input().split())

maps = [ list(map(int, input())) for _ in range(N)]
res = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def DFS(ci, cj):
    maps[ci][cj] = 1
    
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        
        if not(0 <= ni < N and 0 <= nj < M):
            continue
        
        if maps[ni][nj]:
            continue
        
        DFS(ni, nj)
    

for i in range(N):
    for j in range(M):
        if maps[i][j]:
            continue
        res += 1
        DFS(i,j)

print(res)