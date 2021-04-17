"""
문제 링크: https://www.acmicpc.net/problem/11055
문제 접근 방법: dp
"""

N = int(input())

num = list(map(int, input().split()))
arr = []
dp = []
for n in num:
    arr.append(n)
    dp.append(n)

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))