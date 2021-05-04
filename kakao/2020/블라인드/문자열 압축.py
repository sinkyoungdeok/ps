"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60057
문제 접근 방법: 구현
"""
def zip(s, size):
    res = ""
    i = 0
    while i < len(s):
        temp = s[i:i+size]
        cnt = 1
        for j in range(i+size, len(s), size):
            if temp == s[j:j+size]:
                cnt+=1
            else:
                break
        if cnt == 1:
            res += temp
            i += (size)
        else:
            res += str(cnt) + temp
            i += (size*cnt)
    return res



def solution(s):
    answer = 100000000
    for i in range(1,len(s)+1):
        res = zip(s, i)
        if len(res) < answer:
            answer = len(res)
    return answer

s = "xababcdcdababcdcd"
print(solution(s))