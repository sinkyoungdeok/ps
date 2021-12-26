
def pi(pattern):
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(s, pattern):
    pi_list = pi(pattern)
    res = 0 
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi_list[j-1]

        
        if s[i] == pattern[j]:
            if j == (len(pattern)-1):
                res +=1
                j = pi_list[j]
            else:
                j+=1
    return res

A = input()
B = input()

A += A[:-1]

print(kmp(A,B))


