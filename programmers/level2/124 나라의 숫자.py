"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12899
문제 접근 방법: 진법
"""

def solution(n):
    answer = ""
    
    num_list = ["4","1","2"]
    
    while(n):
        answer = num_list[n%3] + answer
        
        if n %3 ==0 :
            n = int(n/3) - 1
        else:
            n = int(n/3)
            
    
    return answer