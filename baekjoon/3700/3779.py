
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


T = 1

while True:
    N = int(input())
    if N == 0: 
        break 
    S = input()

    pi_list = pi(S)

    print("Test case #" + str(T))
    
    for i in range(1, N):
        p = pi_list[i]
        r = i+1 - p
        if p and p%r ==0:
            print(i+1, p//r +1)
    
    print()


    T += 1
