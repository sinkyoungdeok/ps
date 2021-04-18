"""
문제 링크: https://www.acmicpc.net/problem/11722
문제 접근 방법: dp
"""

N = int(input())


A = list(map(int,input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j] +1 )

print(max(dp))