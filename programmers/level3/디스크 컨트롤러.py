"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42627
문제 접근 방법: 힙(우선순위큐)
"""

import heapq

def solution(jobs):
    answer = 0
    i = 0
    start = -1
    now = 0

    pq = []
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(pq, (job[1],job[0]))
        if len(pq) > 0:
            curr = heapq.heappop(pq)
            start = now
            now += curr[0]
            answer += now - curr[1]
            i +=1
        else:
            now +=1



    return answer//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))