"""
문제 링크: https://www.acmicpc.net/problem/12920
문제 접근: 방법: dp 
"""

N, M = map(int, input().split())

dp = [0] * (M+1)
V, C = [], []
for _ in range(N):
    v,c,k = map(int, input().split())

    i = 1
    while k:
        temp = min(i, k)

        V.append(temp * v)
        C.append(temp * c)

        i *= 2
        k -= temp

for i in range(len(V)):
    for j in range(M, 0, -1):
        if j >= V[i]:
            dp[j] = max(dp[j], dp[j-V[i]] + C[i])

print(dp[M])

    