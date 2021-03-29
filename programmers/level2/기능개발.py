"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42586
문제 접근 방법: 단순 구현
"""

def solution(progresses, speeds):
    answer = []
    
    date = 0
    i = 0
    day = 0

    while i < len(progresses):
        progress = progresses[i]
        speed = speeds[i]
        
        if progress + date * speed >= 100:
            i+=1
            day += 1
        elif day > 0:
            answer.append(day)
            day = 0
            date+=1
        else:
            date+=1
    answer.append(day)
            
    return answer