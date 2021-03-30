"""
문제 링크: https://www.acmicpc.net/problem/16953
문제 접근 방법: bfs
"""

from collections import deque 

A,B = map(int, input().split())

q = deque()
q.append((A, 1))

make_check = False
while q:
    curr = q.popleft()
    curr_value,cnt = curr[0], curr[1]
    if curr_value == B:
        print(cnt)
        make_check = True

    product_next = curr_value * 2
    if product_next <= B:
        q.append((product_next, cnt+1))
    
    one_next = curr_value * 10 + 1
    if one_next <= B:
        q.append((one_next,cnt+1))
    

if not make_check:
    print(-1)     