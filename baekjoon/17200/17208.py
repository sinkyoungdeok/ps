"""
문제 링크: https://www.acmicpc.net/problem/17208
문제 접근 방법: dp + 배낭
"""

N,M,K = map(int,input().split())

x, y = [0],[0]
dp = [[[0 for _ in range(301)] for _ in range(301)] for _ in range(101)]
for _ in range(N):
    x_,y_ = map(int,input().split())
    x.append(x_)
    y.append(y_)

for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, K+1):
            if j >= x[i] and k >= y[i]:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-x[i]][k-y[i]] +1)
            else:
                dp[i][j][k] = dp[i-1][j][k] 

print(dp[i][j][k])
