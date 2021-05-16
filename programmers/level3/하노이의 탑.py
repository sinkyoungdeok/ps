"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12946
문제 접근 방법: dfs
"""

def hanoi(n, froms, to, temp,ans):
    if n == 1:
        ans.append([froms,to])
        return
    
    hanoi(n-1, froms, temp, to,ans)

    ans.append([froms,to])

    hanoi(n-1, temp, to, froms,ans)

def solution(n):
    answer = []

    hanoi(n, 1, 3, 2, answer)


    return answer

n = 2
print(solution(n))