def solution(s):
    cnt = 0
    for i in s:
        if cnt < 0:
            break
        cnt = cnt+1 if i=="(" else cnt-1 if i==")" else cnt
        
    return cnt==0