"""
문제 링크: https://www.acmicpc.net/problem/4963
문제 접근 방법: bfs , dfs(재귀함수) 로 접근했다가 python의 stack메모리가 작아서 런타임 에러 뜨는 것을 발견하여 bfs로 방법을 바꿔서 풀었다.
"""

from collections import deque

di = [1,1,1,-1,-1,-1,0,0]
dj = [0,-1,1,0,-1,1,-1,1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    board = []
    for _ in range(h):
        board.append(list(map(int,input().split())))

    res = 0
    q = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                board[i][j] = 0
                res +=1
                
                q.append((i,j))
                while q:
                    ci, cj = q.popleft()


                    for d in range(8):
                        ni = ci + di[d]
                        nj = cj + dj[d]

                        if 0 <= ni < h and 0 <= nj < w and board[ni][nj] == 1:
                            board[ni][nj] = 0
                            q.append((ni,nj))
    print(res)

