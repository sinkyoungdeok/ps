n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = board[0][0]

for i in range(0, n -1 ):
    for j in range(i + 1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + board[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + board[i+1][j+1])

print(max(dp[n-1]))
