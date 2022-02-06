from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
res = 0


def bfs(ci, cj):
    q = deque()
    q.append((ci, cj))
    moving_people = [(ci, cj)]
    while q:
        curr_i, curr_j = q.popleft()
        for d in range(4):
            ni = curr_i + di[d]
            nj = curr_j + dj[d]
            if not (0 <= ni < N and 0 <= nj < N): continue
            if visited[ni][nj]: continue
            if not (L <= abs(board[ni][nj] - board[curr_i][curr_j]) <= R): continue
            visited[ni][nj] = True
            q.append((ni, nj))
            moving_people.append((ni, nj))
    return moving_people


while True:
    visited = [[False] * N for _ in range(N)]
    check = True
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            visited[i][j] = True
            moving = bfs(i, j)
            if len(moving) <= 1: continue

            check = False
            moving_res = sum([board[mi][mj] for mi, mj in moving]) // len(moving)
            for mi, mj in moving:
                board[mi][mj] = moving_res
    if check:
        break
    res += 1

print(res)
