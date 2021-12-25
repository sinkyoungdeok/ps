string = input()

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

ans = 0
for i in range(len(string)):
    ans = max(ans, max(pi(string[i:])))

print(ans)