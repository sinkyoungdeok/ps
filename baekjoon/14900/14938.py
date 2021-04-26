"""
문제 링크: https://www.acmicpc.net/problem/14938
문제 접근: 방법: 플로이드-와샬
"""

n,m,r = map(int,input().split())
item_list = list(map(int,input().split()))
INF = 100000000000000
F = [[INF] * n for _ in range(n)]

for _ in range(r):
    a,b,l = map(int,input().split())
    F[a-1][b-1] = l
    F[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            F[i][j] = min(F[i][j], F[i][k] + F[k][j])

res = -1
for i in range(n):
    sum = 0
    F[i][i] = 0
    
    for j in range(n):
        if F[i][j] <= m:
            sum += item_list[j]
    res = max(res, sum)
print(res)