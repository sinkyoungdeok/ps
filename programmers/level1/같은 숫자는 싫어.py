def solution(arr):
    answer = []
    
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    
    return answer