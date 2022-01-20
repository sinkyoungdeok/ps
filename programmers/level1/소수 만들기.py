from itertools import combinations 

def is_prime(sum): 
    for i in range(2, sum): 
        if sum % i == 0 : 
            return False 
    return True 

def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for i in A: 
        if is_prime(i[0] +i[1]+ i[2]): 
            answer += 1
    return answer