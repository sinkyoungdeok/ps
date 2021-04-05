"""
문제 링크: https://www.acmicpc.net/problem/2210
문제 접근 방법: dfs + 브루트포스
"""
from collections import deque

board = []
for _ in range(5):
    board.append(list(input().split()))

res = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(5):
    for j in range(5):
        st = deque()
        st.append( (i,j, board[i][j]))
        while st:
            curr = st.pop()
            ci = curr[0]
            cj = curr[1]
            curr_str = curr[2]

            if len(curr_str) == 6:
                res.append(curr_str)
            else:
                for d in range(4):
                    ni = ci + dx[d]
                    nj = cj + dy[d]
                    
                    if 0<=ni <5 and 0 <= nj < 5:
                        st.append((ni,nj, curr_str+board[ni][nj]))
            
            
print(len(set(res)))