"""
문제 링크: https://www.acmicpc.net/problem/11404
문제 접근 방법: 플로이드 와샬 
"""

n = int(input())
m = int(input())

INF = 200000000
F = [[INF] * n for _ in range(n) ]

for i in range(n):
    F[i][i] = 0

for i in range(m):
    a,b,c = map(int,input().split())
    if F[a-1][b-1] > c:
        F[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            F[i][j] = min(F[i][j], F[i][k] + F[k][j])

for i in range(n):
    for j in range(n):
        if F[i][j] == INF:
            F[i][j] = 0
    print(*F[i])