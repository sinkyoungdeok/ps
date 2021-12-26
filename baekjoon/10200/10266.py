
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

N = int(input())
A1 = [False] * 360000
A2 = [False] * 360000

for a1 in map(int, input().split()):
    A1[a1] = True

for a2 in map(int, input().split()):
    A2[a2] = True

A1 += A1 

if kmp(A1, A2):
    print("possible")
else:
    print("impossible")

