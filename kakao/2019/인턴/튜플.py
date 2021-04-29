"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/64065
문제 접근 방법: 단순 구현
"""
import json
def solution(s):
    s = s[2:]
    s = s[:-2]
    s = s.split("},{")
    for i in range(len(s)):
        temp = list(map(int,s[i].split(",")))
        s[i] = (len(temp),temp)
    s.sort()

    answer = []
    for _, s_list in s:
        for num in s_list:
            if not num in answer:
                answer.append(num)
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"	))