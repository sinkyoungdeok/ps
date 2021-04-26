"""
문제 링크: https://www.acmicpc.net/problem/11404
문제 접근 방법: 플로이드 와샬 
"""

INF = 200000000
N = int(input())

F = [ list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if F[i][j] == 0:
            F[i][j] = INF 

for k in range(N):
    for i in range(N):
        for j in range(N):
            F[i][j] = min(F[i][j], F[i][k] + F[k][j])

for i in range(N):
    for j in range(N):
        if F[i][j] == INF:
            F[i][j] = 0
        else:
            F[i][j] = 1
    print(*F[i])