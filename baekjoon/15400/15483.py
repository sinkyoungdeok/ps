A = input()
B = input()

alen = len(A) + 1
blen = len(B) + 1

dp = [[0] * blen for _ in range(alen)]
for i in range(1, alen):
    dp[i][0] = dp[i - 1][0] + 1

for i in range(1, blen):
    dp[0][i] = dp[0][i - 1] + 1

for i in range(1, alen):
    for j in range(1, blen):
        cost = 0 if A[i - 1] == B[j - 1] else 1

        dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + cost)

print(dp[alen-1][blen-1])
