def solution(n, k):
    answer = 0
    primes = get_prime_list()

    k_number = int_to_k(n, k)
    
    print(k_number)

    if '0' not in k_number:
        return 1

    for i in k_number.split("0"):
        if i != '' and  int(i) in primes:
            answer += 1

        
    return answer


def int_to_k(n, k):
    if k == 10:
        return str(int(n))
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(int(mod))
    return rev_base[::-1]


def get_prime_list():
    n = 10000
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes