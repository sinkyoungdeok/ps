"""
문제 링크: https://www.acmicpc.net/problem/1535
문제 접근 방법: dp + 배낭
"""

N = int(input())
K = 99

L, J = [0], [0]

for l in input().split():
    L.append(int(l))
for j in input().split():
    J.append(int(j))


dp = [[0] * 100 for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if j >= L[i]:
            dp[i][j] = max(dp[i-1][j], J[i] + dp[i-1][j - L[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(max(dp[i]))