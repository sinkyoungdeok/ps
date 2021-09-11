from collections import deque


def solution(n, info):
    answer = []

    q = deque()

    q.append((0, [], 0, n))

    ans = 0
    while q:
        curr_i, curr_info, curr_sum, curr_arrow = q.popleft()

        if curr_i > 10:
            if curr_arrow > 0:
                curr_info[10] = curr_arrow
            apeach = 0
            rion = 0
            for i in range(11):
                if curr_info[i] <= info[i] and info[i] > 0:
                    apeach += 10 - i
                elif curr_info[i] > info[i] and curr_info[i] > 0:
                    rion += 10 - i

            sub = rion - apeach
            if sub > 0 and ans <= sub:
                # print(curr_info, sub, ans)
                if ans == sub:
                    
                    for i in range(10, -1, -1):
                        if curr_info[i] > answer[i]:
                            answer = curr_info
                            break
                        elif curr_info[i] < answer[i]:
                            break
                    
                else:
                    ans = sub
                    answer = curr_info
                


            continue

        for i in range(2):
            if i == 0:
                next_i = curr_i + 1
                next_info = list(curr_info)
                next_info.append(0)
                next_sum = curr_sum
                next_arrow = curr_arrow
                q.append((next_i, next_info, next_sum, next_arrow))

            elif curr_arrow > 0 and curr_arrow >= (info[curr_i] + 1):
                next_i = curr_i + 1
                next_info = list(curr_info)
                next_info.append(info[curr_i] + 1)
                next_sum = curr_sum + (10 - curr_i)
                next_arrow = curr_arrow - (info[curr_i] + 1)
                q.append((next_i, next_info, next_sum, next_arrow))

    if len(answer) == 0:
        return [-1]
    return answer