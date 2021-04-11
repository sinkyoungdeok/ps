"""
문제 링크: https://www.acmicpc.net/problem/9251
문제 접근: 방법: dp 
"""

A = list(input())
B = list(input())

dp = [[0] * (len(B)+1) for _ in range(len(A) + 1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[i][j])