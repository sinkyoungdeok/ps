"""
문제 링크: https://www.acmicpc.net/problem/5567
문제 접근 방법: bfs
"""
from collections import deque
n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


q = deque()
q.append(1)
visited[1] = True

depth = 0
res = 0

while q:
    depth +=1

    for _ in range(len(q)):
        curr = q.popleft()
        for e in adj[curr]:
            if not visited[e]:
                visited[e] = True
                q.append(e)
                res +=1
    if depth == 2:
        break

print(res)
