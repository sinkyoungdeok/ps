"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72410
문제 접근 방법: 구현
"""

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if 'a'<= i <= 'z' or '0' <= i <= '9' or i == '-' or i == '_' or i =='.':
            answer+=i
    new_id = answer

    # 3
    while new_id.find('..') > -1:
        new_id = new_id.replace("..",".")
    answer = new_id

    # 4
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) >0 and answer[-1] == '.':
        answer = answer[:-1]

    # 5
    if len(answer) == 0:
        answer = 'a'

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7
    while len(answer) <= 2:
        answer += answer[-1]


    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))