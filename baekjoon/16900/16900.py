
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


S, K = input().split()
K = int(K)

pi_list = pi(S)
N = len(S)
ans = N + (N - pi_list[N-1]) * (K-1)

print(ans)
