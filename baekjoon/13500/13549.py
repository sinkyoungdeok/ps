"""
문제 링크: https://www.acmicpc.net/problem/13549
문제 접근 방법: 다익스트라
"""

import heapq

N, K = map(int,input().split())

INF = 100001
res_table = [INF] * (100001)
res_table[N] = 0

pq = []
heapq.heappush( pq, (0, N))

while pq:
    cw, cv = heapq.heappop(pq)

    if res_table[cv] < cw :
        continue

    for i in range(3):
        if i == 0:
            nv = cv + 1
        elif i == 1:
            nv = cv - 1
        else:
            nv = cv * 2
        
        if not 0 <= nv < INF:
            continue
        if res_table[nv] <= res_table[cv]:
            continue

        if i < 2 :
            heapq.heappush(pq, (cw+1, nv))
            res_table[nv] = cw + 1
        else:
            heapq.heappush(pq, (cw, nv))
            res_table[nv] = cw

print(res_table[K])