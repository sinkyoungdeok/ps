import heapq

N, K = map(int, input().split())

min_pq = []
max_pq = []
C = []
ans = 0

for _ in range(N):
    heapq.heappush(min_pq, list(map(int, input().split())))

for _ in range(K):
    C.append(int(input()))

C.sort()

for c in C:
    while min_pq and min_pq[0][0] <= c:
        heapq.heappush(max_pq, -heapq.heappop(min_pq)[1])
    
    if max_pq:
        ans += abs(heapq.heappop(max_pq))

print(ans)