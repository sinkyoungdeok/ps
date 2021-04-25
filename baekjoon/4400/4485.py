"""
문제 링크: https://www.acmicpc.net/problem/4485
문제 접근 방법: 다익스트라
"""

import heapq

di = [0,0,1,-1]
dj = [1,-1,0,0]

T = 0
while True:
    INF = float("INF")
    T += 1
    N = int(input())
    if N == 0:
        break
    miro = [ list(map(int,input().split())) for _ in range(N)]
    res = [[INF] * (N) for _ in range(N)]

    pq = []
    heapq.heappush(pq, (miro[0][0], 0,0))
    res[0][0] = miro[0][0]

    while pq:
        m, ci, cj = heapq.heappop(pq)

        if res[ci][cj] < m:
            continue

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if res[ni][nj] <= m + miro[ni][nj]:
                continue

            res[ni][nj] = m + miro[ni][nj]
            heapq.heappush(pq, (m+miro[ni][nj], ni, nj))
    print("Problem " +str(T)+":" ,res[N-1][N-1])