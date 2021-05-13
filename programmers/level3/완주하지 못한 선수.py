"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42576
문제 접근 방법: 해시
"""

def solution(participant, completion):
    answer = ''

    dic = {}
    for p in participant:
        if dic.get(p):
            dic[p] +=1
        else:
            dic[p] = 1

    for c in completion:
        if dic.get(c):
            dic[c] -=1

    for k,v in dic.items():
        if v != 0:
            answer = k

    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant,completion))
