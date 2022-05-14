numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def getBinaryNum(n, ans, base):
    
    a = n // base
    b = n % base
    
    ans = numbers[b] + ans
    if a == 0 :
        return ans
    else :
        return getBinaryNum(a, ans, base)

def solution(n, t, m, p):
    answer = ''
    
    i = 0 
    turn = 0
    while len(answer) < t:
        convert_num = getBinaryNum(i, "", n)
        
        for cn in convert_num:
            if turn+1 == p:
                answer += cn
            turn += 1 
            turn %= m
        
        i += 1
    
    return answer[:t]