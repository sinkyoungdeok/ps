n = int(input())
T = []
P = []
dp = []
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    dp.append(p)

dp.append(0)
for i in range(n - 1, -1, -1):
    if T[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
print(dp[0])