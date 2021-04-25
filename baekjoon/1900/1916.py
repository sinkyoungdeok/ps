"""
문제 링크: https://www.acmicpc.net/problem/1916
문제 접근 방법: 다익스트라
"""
import heapq

N = int(input())
M = int(input())

INF = float("INF")
graph = [[] for _ in range(N+1) ]
pq = [] 
res_table = [INF] * (N+1)

for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

start,end = map(int,input().split())

res_table[start] = 0
heapq.heappush( pq, (0, start) )

while pq:
    cw, cv = heapq.heappop(pq)
    
    if res_table[cv] < cw:
        continue

    for nv, nw in graph[cv]:
        if res_table[nv] > cw + nw:
            res_table[nv] = cw + nw
            heapq.heappush( pq, (cw+nw, nv))

print(res_table[end])