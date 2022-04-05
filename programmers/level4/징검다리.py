def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    l, r  = 0, 1000000000
    while l <= r:
        m = (l+r) // 2
        
        min_value = 1000000000000
        curr = 0
        cnt = 0
        
        for i in rocks:
            if (i - curr) < m:
                cnt += 1
            else:
                min_value = min(min_value, i - curr)
                curr = i
                
        if cnt <= n:
            answer = min_value
            l = m + 1
        else:
            r = m - 1
    
    return answer