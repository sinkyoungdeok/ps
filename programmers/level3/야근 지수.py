import heapq 
def solution(n, works):
    answer = 0
    pq = []
    
    for i in works:
        heapq.heappush(pq, (-i))
    
    for _ in range(n):
        work = -heapq.heappop(pq) - 1
        heapq.heappush(pq, (-work))
    
    for i in pq:
        if i > 0:
            continue
        answer += i ** 2
        
    
    return answer