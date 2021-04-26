"""
문제 링크: https://www.acmicpc.net/problem/1956
문제 접근: 방법: 플로이드-와샬
"""

V, E = map(int, input().split())

INF = 100000000000
F = [[INF]*V for _ in range(V)]

for i in range(E):
    a,b,c = map(int, input().split())
    F[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            F[i][j] = min(F[i][j], F[i][k] + F[k][j])
            
res = INF
for i in range(V):
    res = min(res, F[i][i])

if res == INF:
    print(-1)
else:
    print(res)