"""
문제 링크: https://www.acmicpc.net/problem/1946
문제 접근: 방법: 그리디
"""

T = int(input())

for _ in range(T):
    N = int(input())

    score = []
    for _ in range(N):
        a,b = map(int,input().split())
        score.append((a,b))
    
    score = sorted(score, key = lambda x: x[0])

    res = 1
    min_score = score[0][1]
    for i in range(1, N):
        if min_score >= score[i][1]:
            min_score = score[i][1]
            res +=1
    
    print(res)