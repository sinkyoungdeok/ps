"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/49191
문제 접근 방법: bfs
"""

from collections import deque

def solution(n, results):
    answer = 0
    adj = [[] for _ in range(n+1)]
    for i,j in results:
        adj[i].append(j)
    visit_list = []
    visit_list.append([1])
    for i in range(1,n+1):
        visited = [False] * (n+1)

        visited[i] = True
        visited[0] = True

        q = deque()
        q.append(i)
        while q:
            curr = q.popleft()
            
            for next in adj[curr]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
        
        visit_list.append(visited)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if visit_list[i][j]:
                visit_list[j][i] = True
            if visit_list[j][i]:
                visit_list[i][j] = True
        if not (False in visit_list[i]):
            answer+=1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	
print(solution(n,results))