"""
문제 링크: https://www.acmicpc.net/problem/2665
문제 접근 방법: 다익스트라
"""

import heapq

di = [0,0,1,-1]
dj = [1,-1,0,0]
n = int(input())

miro = [ list(map(int,input())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        miro[i][j] ^= 1

INF = float("INF")
res = [[INF] * (n) for _ in range(n)]
pq = []
heapq.heappush(pq, (miro[0][0],0,0))
res[0][0] = miro[0][0]
while pq:
    cnt, ci, cj = heapq.heappop(pq)

    if res[ci][cj] < cnt:
        continue

    for d in range(4):
        ni, nj = ci+di[d], cj+dj[d]

        if not(0<=ni<n and 0<=nj<n):
            continue
        if res[ni][nj] <= cnt + miro[ni][nj]:
            continue

        res[ni][nj] = cnt + miro[ni][nj]
        heapq.heappush(pq, (res[ni][nj], ni, nj))

print(res[n-1][n-1])

    