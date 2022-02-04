from collections import deque

N, M, K, X = map(int, input().split())

X -= 1
adj = [ [] for _ in range(N) ]
visited = [-1] * N

for _ in range(M):
    A, B = map(int, input().split())
    adj[A-1].append(B-1)

q = deque()
q.append((X,0))
visited[X] = 0

while q:
    curr, cnt = q.popleft()

    for next in adj[curr]:
        if visited[next] != -1: continue
        visited[next] = cnt +1
        q.append((next, cnt+1))

if visited.count(K) == 0:
    print(-1)

for i,v in enumerate(visited):
    if v == K:
        print(i+1)