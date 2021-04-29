"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/67258
문제 접근 방법: 
"""

def solution(gems):
    set_size = len(set(gems))
    dic = {gems[0]:1}
    answer = [0, len(gems)-1]
    start, end = 0,0
    gem_size = len(gems)
    while start < gem_size and end < gem_size:
        if len(dic) == set_size:
            if end-start < answer[1] - answer[0]:
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -=1
            start +=1
        else:
            end +=1
            if end == gem_size:
                break
            if dic.get(gems[end]) == None:
                dic[gems[end]] = 1
            else:
                dic[gems[end]] +=1

    
    

    return [answer[0]+1, answer[1]+1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))