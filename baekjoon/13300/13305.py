"""
문제 링크: https://www.acmicpc.net/problem/13305
문제 접근 방법: 브루트포스
"""

N = int(input())

R = list(map(int, input().split()))
L = list(map(int, input().split()))

min_l = L[0]
res = 0
for i in range(len(R)):
    if min_l > L[i]:
        min_l = L[i]
    res += min_l * R[i]

print(res)