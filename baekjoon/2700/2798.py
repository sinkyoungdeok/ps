"""
문제 링크: https://www.acmicpc.net/problem/2798
문제 접근 방법: 브루트포스
"""

from itertools import permutations

N, M = map(int,input().split())
C = list(map(int,input().split()))

per = permutations(C, 3)
res = 0
for p in per:
    sum_ = sum(p)
    if M >= sum_:
        res = max(res, sum_)
print(res)