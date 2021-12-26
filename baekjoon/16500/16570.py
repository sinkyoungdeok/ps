
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

N = int(input())
A = list(input().split())[::-1]

pi_list = pi(A)
maxA = max(pi_list)
cnt = pi_list.count(maxA)

if maxA == 0:
    print(-1)
else:
    print(maxA, cnt)