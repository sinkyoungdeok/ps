def solution(n):
    
    bin_n = str(bin(n))
    
    for i in range(n+1, 10000000):
        bin_i = str(bin(i))
        
        if bin_n.count('1') == bin_i.count('1'):
            return i