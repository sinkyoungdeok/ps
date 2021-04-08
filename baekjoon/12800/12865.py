"""
문제 링크: https://www.acmicpc.net/problem/12865
문제 접근 방법: dp
"""

N, K = map(int, input().split())
W, V = [0], [0]
dp = [[0]*(K+1) for _ in range(N+1) ]
for _ in range(N):
    w,v = map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1, N+1):
    for j in range(1, K+1):
        if W[i] <= j:
            dp[i][j] = max(dp[i-1][j], V[i] + dp[i-1][j-W[i]])
        else:
            dp[i][j] = dp[i-1][j]


print(max(dp[i]))