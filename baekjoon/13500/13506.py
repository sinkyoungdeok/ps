
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
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi_list[j-1]

        
        if s[i] == pattern[j]:
            if j == (len(pattern)-1):
                return True
            else:
                j+=1
    return False

def solve():
    S = input()

    if len(S) <= 2:
        print(-1)
        return 

    pi_list = pi(S)
    pattern = S[len(S) - pi_list[-1]:]
    s = S[1: len(S)-1]

    for i in range(len(pattern)):
        p = pattern[i:]
        temp = S[:len(pattern) -i]

        
        if p == temp and kmp(s, p):
            print(p)
            return 

    print(-1)

solve()