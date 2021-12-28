def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y 

V, E = map(int, input().split())
ABC = []
parent = [ i for i in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    ABC.append((C,A,B))

ABC.sort()
res = 0

for C, A, B in ABC:
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        res += C

print(res)