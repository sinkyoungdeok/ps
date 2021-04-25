"""
문제 링크: https://www.acmicpc.net/problem/1753
문제 접근 방법: 다익스트라
"""
import heapq

V, E = map(int, input().split())
start_node = int(input())

INF = float("INF")
graph = [[] for _ in range(V+1) ]
pq = []
res_table = [INF] * (V+1)
res_table[start_node] = 0
heapq.heappush(pq, (0, start_node))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append( (v,w) )

while pq:
    w, v = heapq.heappop(pq) 
    if res_table[v] < w:
        continue
    for nv, nw in graph[v]:
        if res_table[nv] > w + nw:
            res_table[nv] = w + nw
            heapq.heappush(pq, (w + nw, nv))

for i in range(1, V+1):
    if res_table[i] == INF:
        print("INF")
    else:
        print(res_table[i])