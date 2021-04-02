"""
문제 링크: https://www.acmicpc.net/problem/2644
문제 접근 방법: bfs
"""

from collections import deque 

n = int(input())
start, target = map(int, input().split())
m = int(input())

adj = [ [] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

q = deque()
q.append((start,0))
visited[start] = True

find_check = False
while q:
    curr = q.popleft()
    curr_node, curr_cnt = curr[0], curr[1]

    if target == curr_node:
        print(curr_cnt)
        find_check = True
        break
    
    for v in adj[curr_node]:
        if not visited[v]:
            visited[v] = True
            q.append((v, curr_cnt+1))
    
    


if not find_check:
    print(-1)