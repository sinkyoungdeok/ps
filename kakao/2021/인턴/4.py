from collections import deque
from copy import deepcopy
def solution(n, start, end, roads, traps):
    answer = 1000000000000

    trap_list = [False] * (n+1)

    adj = [[] for _ in range(n+1)]
    adj_trap = [[[] for _ in range(n+1)] for _ in range(n+1)]


    for road in roads:
        adj[road[0]].append([road[1],road[2], 1])
        adj[road[1]].append([road[0],road[2], 0])

    for trap in traps:
        trap_list[trap] = True

    for i in range(1, n+1):
        for c in adj[i]:
            if trap_list[c[0]] :
                if not c[0] in adj_trap[i][c[0]] :
                    adj_trap[i][c[0]].append(c[0])
                if not c[0] in adj_trap[c[0]][i] :
                    adj_trap[c[0]][i].append(c[0])
            if trap_list[i]:
                if not i in adj_trap[i][c[0]] :
                    adj_trap[i][c[0]].append(i)
                if not i in adj_trap[c[0]][i] :
                    adj_trap[c[0]][i].append(i)

    q = deque()
    q.append((start, [], 0))
    while q:
        q_size = len(q)
        for q_i in range(q_size):
            curr, curr_trap, curr_cost = q.popleft()
            if curr == end:
                answer = min(answer, curr_cost)
            for next, cost, is_go in adj[curr]:
                trap_sum = is_go
                for t in curr_trap: # is_go % 2 == 0 이면 갈수없고, is_go % 2 == 1 이면 갈 수 있도록 밟은것에 대해서 +1씩해줌
                    if t in adj_trap[curr][next]:
                        trap_sum += 1
                if trap_sum % 2 == 0:
                    continue

                next_trap = deepcopy(curr_trap)

                if trap_list[next]:
                    next_trap.append(next)


                q.append((next, next_trap, curr_cost + cost))

        if answer != 1000000000000:
            break




    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2,3]
print(solution(n,start,end,roads,traps))
