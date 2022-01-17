from collections import deque

N, M, K, X = map(int, input().split())

adj = [ [] for _ in range(N) ]
dist = [-1] * N

for _ in range(M):
    A,B = map(int, input().split())
    adj[A-1].append(B-1)

q = deque()

q.append((X-1, 0))
dist[X-1] = 0

while q:
    curr, cnt = q.popleft()

    for next in adj[curr]:
        if dist[next] != -1:
            continue
        dist[next] = cnt+1
        q.append((next, cnt+1))

check = False
for i in range(N):
    if dist[i] == K:
        print(i+1)
        check = True

if not check:
    print(-1)