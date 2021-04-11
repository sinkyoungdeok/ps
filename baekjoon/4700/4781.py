"""
문제 링크: https://www.acmicpc.net/problem/4781
문제 접근: 방법: dp + 배낭
부가 설명: python3로는 시간초과 가 떳고, pypy3로는 맞았습니다가 떳다.
"""

while True:
    n, m = map(float, input().split())

    n = int(n)
    m = int(m*100 + 0.5)

    if n ==0 and m ==0:
        break
    
    dp = [0]*(m+1) 

    
    for _ in range(1,n+1):
        C, P = map(float, input().split())
        c = int(C)
        p = int(P * 100 + 0.5)

        for i in range(p, m+1):
            dp[i] = max(dp[i], c + dp[i-p])
    
    print(dp[m])