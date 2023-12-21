from collections import deque

N = int(input())
visited = [False] * 60000001

q = deque()
q.append(2)
q.append(3)
q.append(5)

res = set()
res.add(1)

while q:
    curr = q.popleft()

    if curr > 60000000:
        continue
    if visited[curr]:
        continue

    visited[curr] = True
    res.add(curr)

    q.append(curr * 2)
    q.append(curr * 3)
    q.append(curr * 5)

res = sorted(res)
print(res[N-1])