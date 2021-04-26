"""
문제 링크: https://www.acmicpc.net/problem/1516
문제 접근 방법: 위상 정렬
"""

from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
res = [0] * (N+1)
cost = [0] * (N+1)
degrees = [0] * (N+1)

for i in range(1, N+1):
    num_list = list(map(int, input().split()))
    cost[i] = num_list[0]
    for j in range(1, len(num_list) -1 ):
        graph[num_list[j]].append(i)
        degrees[i] += 1

q = deque()
for i in range(1, N+1):
    if degrees[i] == 0:
        q.append(i)

while q:
    curr = q.popleft()
    res[curr] += cost[curr]

    for ne in graph[curr]:
        degrees[ne] -=1

        res[ne] = max(res[ne], res[curr])
        if degrees[ne] == 0:
            q.append(ne)

for i in range(1, N+1):
    print(res[i])
            
