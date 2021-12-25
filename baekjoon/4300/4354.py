
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

while True:
    s = input()

    if s == '.':
        break
    
    pi_list = pi(s)

    if len(s) % (len(s) - pi_list[-1]) == 0:
        print(len(s) // (len(s) - pi_list[-1]))
    else:
        print(1)