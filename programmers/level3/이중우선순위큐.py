"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42628
문제 접근 방법: heap(우선순위 큐)
"""

import heapq

def solution(operations):
    answer = []
    
    
    max_heap = []
    min_heap = []
    temp = []
    for oper in operations:
        cmd, number = oper.split()
        number = int(number)
        
        if cmd == "I":
            temp.append(number)
        else:
            if len(temp) == 0:
                continue
            
            if number == 1:
                max_heap = list(map(lambda x: -x, temp))
                heapq.heapify(max_heap)
                max_value = heapq.heappop(max_heap)
                temp.remove(-max_value)
            else:
                min_heap = temp[:]
                heapq.heapify(min_heap)
                min_value = heapq.heappop(min_heap)
                temp.remove(min_value)
    if len(temp) == 0:
        return [0,0]
    
    max_heap = list(map(lambda x: -x, temp))
    min_heap = temp[:]
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    
    answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
        
    
    return answer

operations = ["I 16","D 1"]
print(solution(operations))