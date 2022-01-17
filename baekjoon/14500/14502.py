from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int,input().split())
map = [ list(map(int,input().split())) for _ in range(N)]

wall = []
virus = []
blank_cnt = 0
res = 0

def bfs(virus):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    q = deque(virus)
    cnt = 0

    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if temp_map[ni][nj] != 0:
                continue
            temp_map[ni][nj] = 2
            cnt += 1
            q.append((ni,nj))

    return cnt

for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            wall.append((i,j))
            blank_cnt += 1
        elif map[i][j] == 2:
            virus.append((i,j))

for w in combinations(wall, 3):
    temp_map = deepcopy(map)
    for i,j in w:
        temp_map[i][j] = 1

    temp_res = blank_cnt - 3
    temp_res -= bfs(virus)
    res = max(res, temp_res)

print(res)