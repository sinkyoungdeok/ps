def solution(n):
    answer = ''

    while n > 0:
        n, remainder = divmod(n,3)
        answer += str(remainder)
    return int(answer, 3)