def solution(n, times):
    answer = 0
    l = 1
    r = max(times) * n
    while l <= r:
        m = (l+ r) // 2
        cnt = 0
        for i in times:
            cnt += m // i
            if cnt >= n:
                break
        
        if cnt >= n:
            answer = m
            r = m - 1
        else:
            l = m + 1
            
    return answer
