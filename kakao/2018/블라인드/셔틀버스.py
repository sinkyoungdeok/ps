"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17678
문제 접근 방법: 구현
"""

def solution(n, t, m, timetable):
    time_list = []
    for time in timetable:
        hh, mm = map(int,time.split(":"))
        time_list.append(hh * 60 + mm)
    bus_list = []
    bus_start = 9 * 60
    for i in range(n):
        bus_list.append( [i * t + bus_start, []])
    time_list.sort()

    prev_start = 0
    for i in range(n):
        for j in time_list:
            if j <= bus_list[i][0]:
                bus_list[i][1].append(j)
                time_list[time_list.index(j)] = 24 * 60
            if len(bus_list[i][1]) == m:
                break
        prev_start = bus_list[i][0]

    if len(bus_list[n-1][1] ) == m:
        answer = max(bus_list[n-1][1])-1
    else:
        answer = bus_list[n-1][0]
    hh = answer // 60
    mm = answer % 60

    return '%02d:%02d' % (hh, mm)

n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]

print(solution(n,t,m,timetable))