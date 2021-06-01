"""
문제 링크: https://www.acmicpc.net/problem/2573
문제 접근 방법: bfs
"""

from collections import deque
from copy import deepcopy
N, M = map(int,input().split())
B = []
for i in range(N):
    B.append(list(map(int,input().split())))

di = [0,0,1,-1]
dj = [1,-1,0,0]

def zero_check():
    for i in range(N):
        for j in range(M):
            if B[i][j] > 0 :
                return False
    return True

def count_around(ci,cj,temp):
    cnt = 0 
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if 0 <= ni < N and 0 <= nj < M and temp[ni][nj] == 0:
            cnt+=1
    return cnt


def one_year_later():
    temp = deepcopy(B)
    for i in range(N):
        for j in range(M):
            if temp[i][j] != 0:
                B[i][j] -= count_around(i,j,temp)
                if B[i][j] < 0:
                    B[i][j] = 0

def bfs():
    temp = deepcopy(B)
    cnt = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                continue
            cnt+=1
            q.append((i,j))
            temp[i][j] = 0
            while q:
                ci ,cj = q.popleft()
                
                for d in range(4):
                    ni, nj = ci+di[d], cj+dj[d]
                    if 0 <= ni < N and 0 <= nj < M and temp[ni][nj] > 0:
                        q.append((ni,nj))
                        temp[ni][nj] = 0
    if cnt >= 2:
        return True
    else:
        return False
res = 0
while True:
    if zero_check():
        print(0)
        break
    one_year_later()
    res += 1
    two_check = 0
    if bfs():
        print(res)
        break
    
    