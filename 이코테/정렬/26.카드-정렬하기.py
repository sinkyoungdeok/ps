import heapq

N = int(input())
card = [ int(input()) for _ in range(N)]

pq = []
for i in card:
    heapq.heappush(pq, i)

res = 0

while len(pq) >= 2:
    curr1 = heapq.heappop(pq)
    curr2 = heapq.heappop(pq)

    next = curr1 + curr2
    res += next

    heapq.heappush(pq, next)

print(res)