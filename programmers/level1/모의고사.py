"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42840
문제 접근 방법: 완전 탐색
"""

def solution(answers):
    ones = [1,2,3,4,5]
    twos = [2,1,2,3,2,4,2,5]
    threes = [3,3,1,1,2,2,4,4,5,5]
    one_len = 5
    two_len = len(twos)
    three_len = len(threes)

    one_cnt = 0
    two_cnt = 0
    three_cnt = 0

    for i,a in enumerate(answers):
        one = ones[i%one_len]
        two = twos[i%two_len]
        three = threes[i%three_len]
        if one == a:
            one_cnt+=1
        if two == a:
            two_cnt+=1
        if three == a:
            three_cnt +=1

    ans = max(max(one_cnt,two_cnt),three_cnt)
    answer = []
    if ans == one_cnt:
        answer.append(1)
    if ans == two_cnt:
        answer.append(2)
    if ans == three_cnt:
        answer.append(3)
    return answer

answers = [1,2,3,4,5,6,7]
print(solution(answers))