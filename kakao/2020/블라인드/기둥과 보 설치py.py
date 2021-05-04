"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60061
문제 접근 방법: 구현
"""
import copy

def isGood(n, wall, bo ):
    for i in range(1,n+1):
        for j in range(0,n+1):
            if wall[i][j] == 1: # 기둥
                if wall[i-1][j] == 0 and bo[i][j] ==0 and bo[i][j-1] == 0:
                    return False # 밑에 기둥이 없고, 밑에 보가 없을 경우
            if bo[i][j] == 1: # 보
                if wall[i-1][j] == 0 and wall[i-1][j+1] ==0 and (bo[i][j-1] == 0 or bo[i][j+1] ==0):
                    return False # 양쪽밑에 기둥이 없고, 양옆 보가 없을 경우
    return True
def solution(n, build_frame):
    answer = []

    wall = [[0] * (n+1) for _ in range(n+1) ]
    bo = [[0] * (n+1) for _ in range(n+1) ]
    for x,y,a,b in build_frame:
        temp_wall = wall[y][x]
        temp_bo = bo[y][x]
        if b == 1: # 설치
            if a == 0 : # 기둥
                wall[y][x] = 1
            else: # 보
                bo[y][x] = 1
        else:
            if a == 0:
                wall[y][x] = 0
            else:
                bo[y][x] = 0

        if not isGood(n, wall, bo):
            wall[y][x] = temp_wall
            bo[y][x] = temp_bo


    for i in range(n+1):
        for j in range(n+1):
            if wall[i][j] == 1:
                answer.append([j,i,0])
            if bo[i][j] == 1:
                answer.append([j,i,1])
    answer.sort()
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n,build_frame))