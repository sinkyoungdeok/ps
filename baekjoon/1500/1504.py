"""
문제 링크: https://www.acmicpc.net/problem/1504
문제 접근 방법: 다익스트라 
==> 1, v1, v2 3개 각각의 시작점으로 다익스트라를 돌린후,
1에서 v1으로 가는 경로 v1에서 v2로 가는경로 v2에서 n으로 가는 경로 각각을 합치면 1 -> v1 -> v2 -> N의 최소 경로를 알수 있다.
1 -> v2 -> v1 -> N으로도 갈 수 있으니까 두개의 최소값을 구하면 v1,v2경로를 지나는 최소값을 구할 수 있다.
"""

import heapq

N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int,input().split())
INF = float("INF")

def dijkstra(start):
    res_table = [INF] * (N+1)
    res_table[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cw, cv = heapq.heappop(pq)

        if res_table[cv] < cw:
            continue

        for nv, nw in graph[cv]:
            if res_table[nv] > cw + nw:
                res_table[nv] = cw + nw
                heapq.heappush(pq, (cw+nw, nv))
    
    return res_table

one_table = dijkstra(1)
v1_table = dijkstra(v1)
v2_table = dijkstra(v2)

res= min(one_table[v1] + v1_table[v2] + v2_table[N], one_table[v2] + v2_table[v1] + v1_table[N] ) 

if res == INF:
    print(-1)
else:
    print(res)