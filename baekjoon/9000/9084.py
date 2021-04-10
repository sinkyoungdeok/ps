"""
문제 링크: https://www.acmicpc.net/problem/9084
문제 접근 방법: dp + 배낭
"""

T = int(input())

for _ in range(T):
    N = int(input())
    C = list(map(int,input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1
    for i in range(N):
        for j in range(M+1):
            if C[i] <= j:
                dp[j] += dp[j - C[i]]
    
    print(dp[M])
