def solution(n, lost, reserve):
    cnt = [ 0 for _ in range(0, n+2)]
    for i in range(1, n+1):
        cnt[i] = 1
    
    for i in lost:
        cnt[i] -= 1
        
    for i in reserve:
        cnt[i] += 1
    
    for i in range(1, n+1):
        if cnt[i] > 0:
            continue
        if cnt[i-1] > 1:
            cnt[i] += 1
            cnt[i-1] -= 1
        elif cnt[i+1] > 1:
            cnt[i] += 1
            cnt[i+1] -= 1
    
    answer = 0
    for i in range(1, n+1):
        if cnt[i] > 0:
            answer += 1
    
    return answer