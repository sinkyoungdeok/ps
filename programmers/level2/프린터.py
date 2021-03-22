"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42587
문제 접근 방법: 단순 구현
"""

def solution(priorities, location):
    print_list = []
    
    answer = 0
    for i in range(len(priorities)):
        print_list.append((priorities[i],i))
    
    while len(print_list) >=  1:
        pri, loc = print_list[0]
        del print_list[0] 
        
        is_ = False
        for p,l in print_list:
            if pri < p:
                is_ = True
        
        if is_:
            print_list.append((pri,loc))
        elif loc != location:
            answer+=1
        else:
            return answer+1
    