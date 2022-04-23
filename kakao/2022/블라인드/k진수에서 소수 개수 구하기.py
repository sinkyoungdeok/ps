def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 ) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    num = convert_notation(n, k)
    
    temp = 0
    answer = 0
    for i in map(int, num):
        if i > 0:
            temp *= 10 
            temp += i
        else:
            if is_prime(temp):
                answer+=1
            temp = 0
    
    if is_prime(temp):
        answer+=1
    
    return answer