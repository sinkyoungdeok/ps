"""
문제 링크: https://www.acmicpc.net/problem/1080
문제 접근 방법: 그리디
"""

N = int(input())
level = [int(input()) for _ in range(N)]
res = 0
for i in range(N-1, 0, -1):
    if level[i] <= level[i-1]:
        res += (level[i-1] - level[i] +1)
        level[i-1] = level[i] -1
print(res)