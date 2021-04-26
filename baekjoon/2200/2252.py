"""
문제 링크: https://www.acmicpc.net/problem/2252
문제 접근 방법: 위상 정렬
"""

from collections import deque

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    indegree[B] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
res = []
while q:
    curr = q.popleft()
    res.append(curr)

    for ne in graph[curr]:
        indegree[ne] -= 1
        if indegree[ne] == 0:
            q.append(ne)
print(*res)