"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/49189
문제 접근 방법: 그래프, bfs
"""

from collections import deque

def solution(n, edge):
    answer = 0

    adj = [ [] for _ in range(n+1)]
    visited = [False] * (n+1)
    dist = [0] * (n+1)

    for el, er in edge:
        adj[er].append(el)
        adj[el].append(er)

    q = deque()
    q.append((1,0))
    visited[1] = True
    while q:
        curr, curr_cnt = q.popleft()

        dist[curr] = curr_cnt

        for next in adj[curr]:
            if not visited[next]:
                visited[next] = True
                q.append((next,curr_cnt+1))

    return dist.count(max(dist))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))