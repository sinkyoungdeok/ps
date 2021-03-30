"""
문제 링크: https://www.acmicpc.net/problem/7562
문제 접근 방법: bfs
"""

from collections import deque

T = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(T):
    l = int(input())
    start_x, start_y = map(int,input().split(" "))
    end_x, end_y = map(int,input().split(" "))
    board = [ [0] * l for i in range(l)]
    board[start_x][start_y] = 1
    
    q = deque()
    q.append((start_x,start_y,0))
    
    while q:
        curr = q.popleft()
        cx,cy = curr[0], curr[1]
        
        if cx == end_x and cy == end_y:
            print(curr[2])
            break
        
        for i in range(8):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx,ny,curr[2]+1)) 
            

    

