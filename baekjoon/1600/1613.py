"""
문제 링크: https://www.acmicpc.net/problem/1613
문제 접근: 방법: 플로이드-와샬
"""

n, k = map(int, input().split())

INF = 1000000000000
F = [[INF]*n for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    F[a-1][b-1] = 1

for K in range(n):
    for I in range(n):
        for J in range(n):
            F[I][J] = min(F[I][J], F[I][K] + F[K][J])

s = int(input())
for _ in range(s):
    a,b = map(int, input().split())
    if F[a-1][b-1] != INF:
        print(-1)
    elif F[b-1][a-1] != INF:
        print(1)
    else:
        print(0)