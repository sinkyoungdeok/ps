"""
문제 링크: https://www.acmicpc.net/problem/2559
문제 접근 방법: 투 포인터
"""

N, K = map(int,input().split())

t = list(map(int,input().split()))

sum = 0
res = -100000000
for i in range(K):
    sum += t[i]

if sum > res:
    res = sum

for i in range(K, N):
    sum += t[i]
    sum -= t[i-K]
        
    if sum > res:
        res = sum

print(res)