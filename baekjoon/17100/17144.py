"""
문제 링크: https://www.acmicpc.net/problem/17144
문제 접근 방법: 구현 
"""

from copy import deepcopy

di = [1,-1,0, 0]
dj = [0,0, 1,-1]
R, C, T = map(int,input().split())
B = []
cleaner = []

def diffusion():
    temp = [[0] * C for _ in range(R)]
    temp[cui][cuj] = -1
    temp[cdi][cdj] = -1
    for i in range(R):
        for j in range(C):
            if B[i][j] != -1:
                cnt = 0
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0<= ni < R and 0 <= nj < C and B[ni][nj] != -1:
                        temp[ni][nj] += B[i][j] // 5
                        cnt += 1
                temp[i][j] += B[i][j] - (B[i][j] // 5 * cnt)
    return temp

def clean(i, j, direction):
    temp = deepcopy(B)
    ci, cj = i, j+1
    B[ci][cj] = 0
    for d in range(4):
        while True:
            ni = ci + di[direction[d]]
            nj = cj + dj[direction[d]]

            if ni == i and nj == j:
                return  
            
            if 0 <= ni < R and 0 <= nj < C:
                B[ni][nj] = temp[ci][cj]
            else:
                break 
            ci, cj = ni, nj 

for i in range(R):
    temp = list(map(int,input().split()))
    B.append(temp)
    for j in range(C):
        if B[i][j] == -1:
            cleaner.append((i,j))

cui, cuj = cleaner[0]
cdi, cdj = cleaner[1]

for t in range(T):
    B = diffusion()
    clean(cui, cuj, [2, 1, 3, 0])
    clean(cdi, cdj, [2, 0, 3, 1])

B[cui][cuj] = 0
B[cdi][cdj] = 0
res = 0
for i in range(R):
    res += sum(B[i])
print(res)