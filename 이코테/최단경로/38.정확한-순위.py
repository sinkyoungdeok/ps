INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            graph[i][j] = graph[j][i]
        elif graph[j][i] == INF:
            graph[j][i] = graph[i][j]

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            cnt += 1
            break

print(N-cnt)