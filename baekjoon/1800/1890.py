"""
문제 링크: https://www.acmicpc.net/problem/1890
문제 접근 방법: dp
"""

N = int(input())

B = []
for _ in range(N):
    B.append( list(map(int,input().split())) )
dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        ni = i + B[i][j]
        nj = j + B[i][j]
        if ni < N:
            dp[ni][j] += dp[i][j]
        if nj < N:
            dp[i][nj] += dp[i][j]

print(dp[i][j])