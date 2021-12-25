from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()

for i in range(N):
    while dq and dq[-1][0] > A[i]:
        dq.pop()
    while dq and dq[0][1] < i - L + 1:
        dq.popleft()
    dq.append((A[i],i))
    print(dq[0][0], end = ' ')
