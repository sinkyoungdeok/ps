from collections import deque


def solution(cacheSize, cities):
    s = set()
    q = []
    answer = 0
    
    for i in cities:
        i = i.lower()
        
        if i in s:
            answer += 1
            q.remove(i)
            q.append(i)
            continue 
        
        answer += 5
        
        if 0 == cacheSize:
            continue
        
        if len(q) == cacheSize:
            temp = q[0]
            del q[0]
            s.remove(temp)
            
        q.append(i)
        s.add(i)
            
    return answer