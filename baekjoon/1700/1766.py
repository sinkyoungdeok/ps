"""
문제 링크: https://www.acmicpc.net/problem/1766
문제 접근 방법: 위상 정렬
"""

import heapq

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    indegree[B] += 1

pq = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

res = []
while pq:
    curr = heapq.heappop(pq)

    res.append(curr)

    for ne in graph[curr]:
        indegree[ne] -=1
        if indegree[ne] == 0:
            heapq.heappush(pq,ne)
print(*res)