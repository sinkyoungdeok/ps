"""
문제 링크: https://www.acmicpc.net/problem/1463
문제 접근 방법: dp
"""

N = int(input())

dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i%2 ==0 and dp[i//2] +1 < dp[i]:
        dp[i] = dp[i//2] +1
    if i%3 ==0 and dp[i//3] +1 < dp[i]:
        dp[i] = dp[i//3] +1

print(dp[N])