"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/64062
문제 접근 방법: parametric search
"""

def start(stones, k ,m):
    cnt = 0
    for s in stones:
        if s - m +1 <= 0:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    l = 1
    r = 200000000
    answer = 0
    while l <= r:
        m = int((l + r) / 2)
        if start(stones,k,m):
            answer = m
            l = m +1
        else:
            r = m -1
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones,k))