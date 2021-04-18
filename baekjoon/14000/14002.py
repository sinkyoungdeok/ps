"""
문제 링크: https://www.acmicpc.net/problem/14002
문제 접근 방법: dp
"""

N = int(input())


nums = list(map(int,input().split()))

dp = []
A = []

for num in nums:
    dp.append([num])
    A.append(num)

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            temp = dp[j] + [A[i]]
            if len(temp) > len(dp[i]):
                dp[i] = temp

max_i = -1
max_v = -1
for i in range(len(dp)):
    if max_v < len(dp[i]):
        max_v = len(dp[i])
        max_i = i

print(max_v)
for i in dp[max_i]:
    print(i, end=' ')
    

