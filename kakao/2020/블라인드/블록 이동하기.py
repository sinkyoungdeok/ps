"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60063
문제 접근 방법: bfs
"""
from collections import deque

# 수평일땐 l이 왼쪽에 있게 고정
# 수직일땐 l이 위쪽에 있게 고정
def solution(board):
    answer = 0

    n = len(board)
    q = deque()
    q.append([(0,0),(0,1),0])

    dic = {}

    while q:
        curr = q.popleft()
        cl, cr, cnt = curr[0], curr[1], curr[2]
        cli, clj, cri, crj = cl[0], cl[1], cr[0], cr[1]

        if dic.get((cl,cr)):
            continue
        else:
            dic[(cl,cr)] = cnt

        if cl == (n-1,n-1) or cr == (n-1,n-1):
            answer = cnt
            break

        if cli == cri : # 수평으로 있는경우
            if (cli +1) < n and (cri + 1) < n:
                if (board[cli+1][clj] + board[cri+1][crj]) == 0: # 밑으로 내릴수있을때
                    q.append([(cli+1,clj),(cri+1,crj),cnt+1]) # 밑으로 내림
                    q.append([(cli,clj),(cli+1,clj),cnt+1]) # 왼쪽밑으로 돌림
                    q.append([(cri,crj),(cri+1,crj),cnt+1]) # 오른쪽밑으로 돌림
            if crj + 1 < n and board[cri][crj+1] == 0: # 오른쪽 으로 갈수있을때
                q.append([(cli,clj+1),(cri,crj+1),cnt+1])
            if cli -1 >= 0 and cri - 1 >= 0:
                if (board[cli-1][clj] + board[cri-1][crj]) == 0: # 위로 올릴 수 있을 때
                    q.append([(cli-1,clj),(cri-1,crj),cnt+1]) # 위로 올림
                    q.append([(cli-1,clj),(cli,clj),cnt+1]) # 왼쪽 위로 돌림
                    q.append([(cri-1,crj),(cri,crj),cnt+1]) # 오른쪽 위로 돌림
            if clj -1 >= 0 and board[cli][clj-1] == 0: #왼쪽
                q.append([(cli,clj-1),(cri,crj-1),cnt+1])
        elif clj == crj: #수직으로 있는경우
            if clj+1 < n and crj + 1 < n:
                if (board[cli][clj+1] + board[cri][crj+1] == 0): # 오른쪽으로 갈 수 있을때
                    q.append([(cli,clj+1),(cri,crj+1),cnt+1]) # 오른쪽
                    q.append([(cli,clj),(cli,clj+1),cnt+1]) # 오른쪽 위
                    q.append([(cri,crj),(cri,crj+1),cnt+1]) # 오른쪽 아래
            if cri +1 < n and board[cri+1][crj] == 0: # 아래로 내릴수있을때
                q.append([(cli+1,crj),(cri+1,crj),cnt+1])
            if clj-1 >= 0 and crj - 1 >= 0:
                if (board[cli][clj-1] + board[cri][crj-1] == 0): # 왼쪽으로 갈 수 있을때
                    q.append([(cli,clj-1),(cri,crj-1),cnt+1]) # 왼쪽
                    q.append([(cli,clj-1),(cli,clj),cnt+1]) # 왼쪽 위
                    q.append([(cri,crj-1),(cri,crj),cnt+1]) # 왼쪽 아래
            if cli -1 >= 0 and board[cli-1][clj] == 0:
                q.append([(cli-1,clj),(cri-1,crj),cnt+1])






    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))