"""
문제 링크: https://www.acmicpc.net/problem/15686
문제 접근 방법: 구현
"""

N, M = map(int, input().split())

board = [ list(map(int,input().split())) for _ in range(N) ]

H = []
C = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            H.append( (i,j) )
        elif board[i][j] == 2:
            C.append( (i,j) )

def start( ci, c_list ):
    global res
    if len(c_list) == M:
        sum = 0
        for hi, hj in H:
            min_ = 1000000
            for ci, cj in c_list:
                temp = abs(hi - ci) + abs(hj - cj)
                if temp < min_:
                    min_ = temp
            sum += min_

        if sum < res:
            res = sum
        return 

    else:
        for i in range(ci+1, len(C)):
            temp_c = c_list + [C[i]]
            start( i, temp_c )


res = 1000000
for i in range(len(C)):
    temp_c = [C[i]]
    sum = start( i, temp_c )

print(res)