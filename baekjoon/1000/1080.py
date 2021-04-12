"""
문제 링크: https://www.acmicpc.net/problem/1080
문제 접근 방법: 그리디
"""

N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int,list(input()))))

for _ in range(N):
    B.append(list(map(int,list(input()))))

res = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            res += 1
            for ii in range(3):
                for jj in range(3):
                    A[i+ii][j+jj] ^= 1

check = True

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            check= False

if check:
    print(res)
else:
    print(-1)