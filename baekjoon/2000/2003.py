"""
문제 링크: https://www.acmicpc.net/problem/2003
문제 접근 방법: 두 포인터
"""

N, M = map(int, input().split())

A = list(map(int, input().split()))

start = 0
end = 1
res = 0
sum = A[start]
if sum == M:
    res += 1
while not (start == end == N):
    if sum < M and end < N:
        sum += A[end]
        end +=1
    else:
        sum -= A[start]
        start +=1
    if sum == M:
        res += 1

print(res)