def solution(N, stages):
    check = [0] * (N+1)
    for i in stages:
        check[i-1] +=1
    stage_len = len(stages)
    result = dict()
    for i in range(N):
        if stage_len == 0:
            result[i+1] = 0
        else:
            result[i+1] = check[i]/stage_len
        stage_len -= check[i]
    
    return sorted(result, key=lambda x : result[x], reverse=True)