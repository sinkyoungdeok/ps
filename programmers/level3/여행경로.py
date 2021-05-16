"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/43164
문제 접근 방법: dfs
"""

import heapq
from collections import deque

def solution(tickets):
    answer = []
    
    dic = {}
    for start,end in tickets:
        if dic.get(start):
            heapq.heappush(dic[start], end)
        else:
            temp = []
            heapq.heappush(temp,end)
            dic[start] = temp

    st = deque()
    st.append("ICN")
    answer.append("ICN")
    while st:
        curr = st.pop()

        if dic.get(curr) and len(dic[curr]):
            next = heapq.heappop(dic[curr])
            st.append(next)
            answer.append(next)
        
    

    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))