"""
문제 링크: https://www.acmicpc.net/problem/1149
문제 접근 방법: dp
"""

N = int(input())

rgb = [] 
dp = []
for _ in range(N):
    rgb.append(list(map(int,input().split())))
    dp.append([10000000000000] * 3)

dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]
for i in range(1, N):
    for j in range(0, 3):
        for k in range(0,3):
            if j == k :
                continue
            if dp[i][j] > rgb[i][j] + dp[i-1][k]:
                dp[i][j] = rgb[i][j] + dp[i-1][k]


res = 10000000000
for i in range(3):
    if res > dp[N-1][i]:
        res = dp[N-1][i]

print(res)