N = int(input())
B = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if B[j] > B[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
