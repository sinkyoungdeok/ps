N, M = map(int, input().split())
adj = [set() for i in range(N+1)]
res = 0

for i in range(M):
    u, v = map(int, input().split())
    
    if u > v:
        u, v = v, u
    adj[u].add(v)

for a in adj:
    for i in a:
        res += len(a.intersection(adj[i]))
    
print(res)