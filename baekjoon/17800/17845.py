"""
문제 링크: https://www.acmicpc.net/problem/17845
문제 접근 방법: dp
"""

N, K = map(int, input().split())

dp = [ [0] * (N+1) for _ in range(K+1)]


for i in range(1,K+1):
    I, T = map(int, input().split())
    for j in range(1,N+1):
        if j >= T:
            dp[i][j] = max(dp[i-1][j], I + dp[i-1][j-T])
        else:
            dp[i][j] = dp[i-1][j]


print(max(dp[i]))