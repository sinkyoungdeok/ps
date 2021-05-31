"""
문제 링크: https://www.acmicpc.net/problem/2573
아직 미완성.. 시간초과 뜸 .
"""

from collections import deque
from copy import deepcopy
N, M = map(int,input().split())
B = []
for i in range(N):
    B.append(list(map(int,input().split())))

di = [0,0,1,-1]
dj = [1,-1,0,0]
res = 0
while True:
    temp = deepcopy(B)
    
    two_check = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if temp[i][j] > 0 :
                two_check+=1
                q.append((i,j))
                temp[i][j] = 0
                while q:
                    ci,cj = q.popleft()
                    
                    for d in range(4):
                        ni,nj = ci + di[d], cj+ dj[d]

                        if not ( 0<=ni<N and 0<=nj<M):
                            continue
                        
                        if temp[ni][nj] > 0:
                            q.append((ni,nj))
                            temp[ni][nj] = 0
    if two_check >= 2:
        break

    minus_temp = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if B[i][j] > 0 :
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if not ( 0<=ni<N and 0<=nj<M):
                            continue
                    if B[ni][nj] <= 0 :
                        minus_temp[i][j] -= 1 
    
    for i in range(N):
        for j in range(M):
            B[i][j] += minus_temp[i][j]
            if B[i][j] <= 0:
                B[i][j] = 0
    res += 1

print(res)