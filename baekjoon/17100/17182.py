"""
문제 링크: https://www.acmicpc.net/problem/17182
문제 접근 방법: 플로이드 와샬
"""

N, K = map(int,input().split())
F = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N 
visited[K] = True
min_num = float("INF")

for k in range(N):
    for i in range(N):
        for j in range(N):
            F[i][j] = min(F[i][j], F[i][k] + F[k][j])

def start(i, j, time, depth):
    global min_num
    if depth == N-1:
        min_num = min(min_num, time)
        return
    if time > min_num:
        return
    
    for k in range(N):
        if not visited[k]:
            visited[k] = True
            start(j, k, time + F[j][k], depth+1)
            visited[k] = False

for i in range(N):
    if not visited[i]:
        visited[i] = True
        start(K, i, F[K][i], 1)
        visited[i] = False

print(min_num)
