"""
문제 링크: https://www.acmicpc.net/problem/2003
문제 접근 방법: 두 포인터
"""

def prime(n):
    li = [False, False] + [True for _ in range(n-1)]
    p = []

    for i in range(len(li)):
        if li[i]:
            p.append(i)
            for k in range(i+i, len(li), i):
                li[k] = False
    return p

N = int(input())

if N == 1:
    print(0)
else:
    num_list = prime(N)

    start = 0
    end = 1
    sum = num_list[start]
    res = 0
    if sum == N:
        res +=1

    while not (start == end == len(num_list)):
        if sum < N and end < len(num_list):
            sum += num_list[end]
            end +=1
        else:
            sum -= num_list[start]
            start +=1
        
        if sum == N:
            res +=1
    print(res)