"""
문제 링크: https://www.acmicpc.net/problem/1806
문제 접근 방법: 두 포인터
"""

N, S = map(int, input().split())

num_list = list(map(int,input().split()))


start = 0
end = 1
sum = num_list[start]
res = N
check = False

if sum >= S:
    res = 1

while not ( N == start == end):
    if sum < S and end < N:
        sum += num_list[end]
        end += 1
    else:
        sum -= num_list[start]
        start +=1
    
    if sum >= S:
        res = min(res,end-start)
        check = True
    
if check:
    print(res)
else:
    print(0)