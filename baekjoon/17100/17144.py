"""
문제 링크: https://www.acmicpc.net/problem/17144
문제 접근 방법: 구현 
"""

R, C, T = map(int,input().split())

B_main = [ list(map(int,input().split())) for _ in range(R)]
B_temp = [ [0] * C for _ in range(R) ]

di = [1,-1,0, 0]
dj = [0,0, 1,-1]

clean_up_i = -1
clean_up_j = -1
clean_down_i = -1
clean_down_j = -1
# 공기 청정기의 윗부분 위치 찾기 
for i in range(R):
    for j in range(C):
        if B_main[i][j] == -1:
            clean_up_i = i-1
            clean_up_j = j
            clean_down_i = i
            clean_down_j = j


# 미세먼지 확산 (일단 확산되는 수치들은 B_temp에 저장)
for i in range(R):
    for j in range(C):
        cnt = 0
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < R and 0<= nj < C and B_main[ni][nj] != -1 and B_main[i][j] != -1:
                cnt +=1
                B_temp[ni][nj] += B_main[i][j] // 5
        B_temp[i][j] -= (B_main[i][j] // 5) * cnt 


# 미세먼지 확산 반영
for i in range(R):
    for j in range(C):
        B_main[i][j] += B_temp[i][j]
        B_temp[i][j] = 0 

# 공기 청정기 작동 (위) .. B_temp를 활용해야 할듯
ci = clean_up_i
cj = clean_up_j + 1
temp_cur = B_main[ci][cj]
temp_next = B_main[ci][cj+1]
while cj + 1 < C:
    ni = ci
    nj = cj + 1
    
    temp = B_main[ci][cj]
    B_main[ci][cj] = temp_next
    temp_cur = B_main[ni][nj]
    B_main[ni][nj] = temp_next
    temp_next = 

    cj = nj

for i in B_main:
    print(i)