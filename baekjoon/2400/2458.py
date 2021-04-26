"""
문제 링크: https://www.acmicpc.net/problem/2458
문제 접근 방법: 플로이드 와샬 
"""

N, M = map(int, input().split())

INF = 20000000000
F = [ [INF] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    F[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            F[i][j] = min(F[i][j], F[i][k] + F[k][j])

res = 0 
for i in range(N):
    check = True
    for j in range(N):
        if i == j:
            continue
        if F[i][j] == INF:
            if F[j][i] == INF:
                check = False
    if check:
        res +=1
print(res)