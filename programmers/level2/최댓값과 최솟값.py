def solution(s):
    ans = list(map(int,s.split()))
    answer = str(min(ans)) + " " + str(max(ans)) 
    return answer