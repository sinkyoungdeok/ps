"""
P = 응시자
O = 빈테이블
X = 파티션
맨하탄 거리 ==> d = | x1-x2 | + |y1-y2|
"""
from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def isGood(place):

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                q = deque()
                q.append((i,j,0))
                visited = [[False] * 5 for _ in range(5)]
                visited[i][j] = True
                while q:
                    curr = q.popleft()
                    ci,cj,cnt = curr

                    if cnt > 0 and place[ci][cj] == "P":
                        if i == ci: # 수평으로 있을떄
                            if place[i][(j+cj)//2] != "X":
                                return 0
                        elif j == cj: # 수직으로 있을때
                            if place[(i+ci)//2][j] != "X":
                                return 0
                        else:
                            if not (place[i][cj] == "X" and place[ci][j] == "X"):
                                return 0

                    if cnt ==2 :
                        continue

                    for d in range(4):
                        ni, nj = ci+di[d], cj+dj[d]
                        if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                            visited[ni][nj] = True
                            q.append((ni,nj,cnt+1))
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(isGood(place))

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))