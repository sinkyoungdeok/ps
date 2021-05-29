"""
문제 링크: https://www.acmicpc.net/problem/18111
문제 접근 방법: 브루트 포스
"""

N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
height = 0
res = 1000000000000000000000000
for i in range(257):
    max = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if board[j][k] < i:
                min += (i - board[j][k])
            else:
                max += (board[j][k] - i)
    inven = max + B
    if inven < min:
        continue
    time = 2 * max + min
    if time <= res:
        res = time
        height = i
print(res, height)