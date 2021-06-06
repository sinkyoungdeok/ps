"""
문제 링크: https://www.acmicpc.net/problem/1325
문제 접근 방법: BFS
"""

from collections import deque

N, M = map(int, input().split())

adj = [ [] for _ in range(N+1)]

for i in range(M):
    A, B = map(int,input().split())
    adj[B].append(A)

res = []
for start in range(N,0,-1):
    visited = [False] * (N+1)
    q = deque()
    q.append(start)
    cnt = 0
    visited[start] = True
    while q:
        curr = q.popleft()
        cnt += 1
        for next in adj[curr]:
            if visited[next]:
                continue
            visited[next] = True
            q.append(next)



    res.append((cnt,start))

res = sorted(res, key = lambda x: (-x[0],x[1]))

max_res = res[0][0]

for i, j in res:
    if i == max_res:
        print(j, end = " ")
