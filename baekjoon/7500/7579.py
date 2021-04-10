"""
문제 링크: https://www.acmicpc.net/problem/7579
문제 접근 방법: dp + 배낭
"""

N, M = map(int, input().split())
m = [0] + list(map(int,input().split()))
c = [0] + list(map(int,input().split()))

c_sum = sum(c)
dp = [[0] * (c_sum+1) for _ in range(N+1)]

res = c_sum

for i in range(1,N+1):
    for j in range(1,c_sum+1):
        if j >= c[i]:
            dp[i][j] = max(dp[i-1][j], m[i] + dp[i-1][j-c[i]])
        else:
            dp[i][j] = dp[i-1][j]

        if M <= dp[i][j]:
            res = min(res, j)

print(res)