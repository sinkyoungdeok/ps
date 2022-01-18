from collections import deque
from itertools import combinations
from copy import deepcopy

N, K = map(int, input().split())

board = []
dic = dict()

for k in range(1, K+1):
    dic[k] = []

for i in range(N):
    board.append(list(map(int,input().split())))
    for j,v in enumerate(board[i]):
        if v == 0:
            continue
        dic[v].append((i, j))

S, X, Y = map(int, input().split())

di = [0,0,1,-1]
dj = [1,-1,0,0]

def solve():
    for _ in range(S):
        for k in range(1, K+1):
            st = []
            for ci, cj in dic[k]:
                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]

                    if not ( 0<= ni < N and 0 <= nj < N):
                        continue
                    if board[ni][nj] != 0:
                        continue

                    board[ni][nj] = k
                    st.append((ni,nj))
                    if ni == X-1 and nj == Y-1:
                        return board[ni][nj]
            dic[k] = st
    return board[X-1][Y-1]

print(solve())
