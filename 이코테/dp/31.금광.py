T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    gold_list = list(map(int, input().split()))

    board = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(gold_list[m * i + j])
        board.append(temp)

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        dp[i][0] = board[i][0]

    for j in range(1, m):
        for i in range(n):
            if i > 0:
                dp[i][j] = max(dp[i][j], board[i][j] + dp[i-1][j-1])
            dp[i][j] = max(dp[i][j], board[i][j] + dp[i][j-1])
            if (i + 1) < n:
                dp[i][j] = max(dp[i][j], board[i][j] + dp[i+1][j-1])

    res = 0
    for i in range(n):
        res = max(res, dp[i][m - 1])