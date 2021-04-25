"""
문제 링크: https://www.acmicpc.net/problem/1261
문제 접근 방법: 다익스트라
"""

import heapq

di = [0,0,1,-1]
dj = [1,-1,0,0]
M, N = map(int,input().split())
A = [ list(map(int,input())) for _ in range(N) ]
pq = []
visited = [ [False] * M for _ in range(N)]
visited[0][0] = True
heapq.heappush(pq, (0,0,0))

while pq:
    cnt, ci, cj = heapq.heappop(pq)
    if ci == N-1 and cj == M-1:
        print(cnt)
        break

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            heapq.heappush(pq, (cnt+A[ni][nj] ,ni,nj) )