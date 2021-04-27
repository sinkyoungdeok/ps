"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17676
문제 접근 방법: 구현
"""

def solution(lines):
    answer = 0
    log_list = []
    for line in lines:
        date, S, T = map(str, line.split())
        
        hh, mm, ss = map(str, S.split(":"))
        end_time = int(ss.split(".")[1]) + int(ss.split(".")[0]) * 1000 + int(mm) * 1000 * 60 + int(hh) * 1000 * 3600
        T_time = int(float(T[:-1]) * 1000)
        start_time = end_time - T_time + 1

        log_list.append((start_time, end_time))
        
    for ist, iet in log_list:
        start1, end1 = ist, ist + 999
        start2, end2 = iet, iet + 999
        cnt1, cnt2 = 0, 0
        for jst, jet in log_list:
            if start1 <= jet  and jst <= end1:
                cnt1+=1
            if start2 <= jet  and jst <= end2:
                cnt2+=1
        answer = max(answer, cnt1)
        answer = max(answer, cnt2)



    return answer
