"""
문제 링크: https://www.acmicpc.net/problem/11725
문제 접근 방법: bfs
"""

from collections import deque

N = int(input())
adj = [ [] for _ in range(N+1)]
visited = [False] * (N+1)
res = [0] * (N+1)

for _ in range(N-1):
    x, y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

q = deque()
q.append(1)
while q:
    curr = q.popleft()
    
    for v in adj[curr]:
        if not visited[v]:
            res[v] = curr
            visited[v] = True
            q.append(v)


for i in range(2, N+1):
    print(res[i])