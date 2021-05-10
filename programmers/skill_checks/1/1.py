def solution(strings, n):
    answer = []
    res = []
    for string in strings:
        res.append((string[n],string))
    res.sort()
    for i,j in res:
        answer.append(j)
    return answer

strings = ["sun", "bed", "car"]
n = 1
print(solution(strings,n))