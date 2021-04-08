"""
문제 링크: https://www.acmicpc.net/problem/2606
문제 접근 방법: bfs
"""

from collections import deque
N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

res = 0
q = deque()
q.append(1)
visited[1] = True

while q:
    curr = q.popleft()

    for next in adj[curr]:
        if visited[next]:
            continue
        q.append(next)
        visited[next] = True
        res +=1

print(res)