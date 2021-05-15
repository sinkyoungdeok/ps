"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/43162
문제 접근 방법: dfs
"""

def dfs(adj,visited, i):
    for next in adj[i]:
        if not visited[next]:
            visited[next] = True
            dfs(adj,visited,next)

def solution(n, computers):
    answer = 0
    adj = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i == j:
                continue
            if computers[i][j] :
                adj[i].append(j)

    for i in range(n):
        if not visited[i]:
            dfs(adj,visited,i)
            answer+=1


    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n,computers))