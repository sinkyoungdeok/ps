"""
문제 링크: https://www.acmicpc.net/problem/11779
문제 접근 방법: 다익스트라
"""

import heapq
from copy import deepcopy

n = int(input())
m = int(input())
INF = float("INF")
graph = [[] for _ in range(n+1) ]
path = [[] for _ in range(n+1)]
cost = [INF] * (n+1)
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

start, end = map(int,input().split())
pq = [] 
heapq.heappush(pq, (0, start))

while pq:
    cw, cv = heapq.heappop(pq)

    if cost[cv] < cw:
        continue

    path[cv].append(cv)

    for nv, nw in graph[cv]:
        if cost[nv] > cw + nw:
            cost[nv] = cw+nw
            path[nv] = deepcopy(path[cv])
            heapq.heappush(pq, (cw+nw, nv))

print(cost[end])
print(len(path[end]))
print(*path[end])
