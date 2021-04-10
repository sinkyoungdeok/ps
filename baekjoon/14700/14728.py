"""
문제 링크: https://www.acmicpc.net/problem/14728
문제 접근 방법: dp
"""

N, T = map(int, input().split())
K, S = [0],[0]

dp = [[0]*(T+1) for _ in range(N+1) ]
for _ in range(N):
    k, s = map(int, input().split())
    K.append(k)
    S.append(s)
   

for i in range(N+1):
    for j in range(T+1):
        if K[i] <=j :
            dp[i][j] = max(dp[i-1][j], S[i] + dp[i-1][j-K[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(max(dp[N]))