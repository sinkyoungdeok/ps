"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72414
문제 접근 방법: 누적합 + 투포인터
"""

def str_to_int(str_time):
    hh, mm, ss = map(int,str_time.split(":"))
    return hh * 3600 + mm * 60 + ss

def int_to_str(int_time):
    hh, mm, ss = int_time // 3600, (int_time%3600) // 60, int_time % 60
    return '{:02d}:{:02d}:{:02d}'.format(hh,mm,ss)


def solution(play_time, adv_time, logs):
    play_time_int = str_to_int(play_time)
    adv_time_int = str_to_int(adv_time)

    log_sum = [0] * 360001
    for log in logs:
        log_start, log_end = log.split("-")
        log_start_int, log_end_int = str_to_int(log_start), str_to_int(log_end)

        log_sum[log_start_int] += 1
        log_sum[log_end_int] -= 1

    for i in range(1, play_time_int+1):
        log_sum[i] += log_sum[i-1]
    for i in range(1, play_time_int+1):
        log_sum[i] += log_sum[i-1]

    max_time = 0
    max_adv = log_sum[adv_time_int]
    for start in range(1, play_time_int):
        if start + adv_time_int < play_time_int:
            end = start + adv_time_int
        else:
            end = play_time_int
        sum_adv = log_sum[end] - log_sum[start]
        if max_adv < sum_adv:
            max_adv = sum_adv
            max_time = start + 1
    return int_to_str(max_time)



    answer = ''
    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time,adv_time,logs))