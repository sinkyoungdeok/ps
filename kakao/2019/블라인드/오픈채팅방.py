"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42888
문제 접근 방법: 구현
"""

def solution(record):
    answer = []

    dic = {}
    res = []
    for re in record:
        r = re.split()
        if r[0] == 'Enter' or r[0] == 'Change':
            dic[r[1]] = r[2]

        if not r[0] == 'Change':
            res.append( (r[1],r[0]) )

    for r in res:
        if r[1] == "Enter":
            answer.append(dic[r[0]] + "님이 들어왔습니다.")
        else:
            answer.append(dic[r[0]] + "님이 나갔습니다.")


    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))