"""
문제 링크: https://www.acmicpc.net/problem/1654
문제 접근 방법: 이분 탐색
"""

K, N = map(int,input().split())
k_list = []
for _ in range(K):
    k_list.append(int(input()))


l, r = 1, max(k_list)

while l<=r:
    m = (l+r)//2
    
    sum = 0 
    for k in k_list:
        sum += k // m
    
    if sum >= N:
        l = m+1
    else:
        r = m-1
print(r)