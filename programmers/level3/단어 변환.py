"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/43163
문제 접근 방법: bfs
"""

from collections import deque

def solution(begin, target, words):
    answer = 100000000

    if not target in words:
        return 0
    q = deque()
    q.append((begin,0))
    while q:
        curr, curr_cnt = q.popleft()

        if curr == target:
            return curr_cnt

        if curr_cnt >= 51:
            break

        for word in words:
            cnt = 0
            for i in range(len(curr)):
                if word[i] == curr[i]:
                    cnt+=1
            if cnt == (len(curr)-1):
                q.append((word,curr_cnt+1))



begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin,target,words))