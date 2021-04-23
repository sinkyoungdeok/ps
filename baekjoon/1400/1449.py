"""
문제 링크: https://www.acmicpc.net/problem/1449
문제 접근 방법: 그리디
"""

N, L = map(int,input().split())

water = list(map(int,input().split()))

water.sort()

res = 0
tape = 0
for i in range(N):
    if water[i] <= tape:
        continue
    res += 1
    tape = water[i] + (L-1)

print(res)