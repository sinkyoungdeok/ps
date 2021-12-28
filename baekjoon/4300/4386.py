import math 

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

n = int(input())
parent =  [ i for i in range(n+1)]

xy = []
abc = []

for _ in range(n):
    x, y = map(float, input().split())
    xy.append((x,y))

for i in range(n-1):
    for j in range(i+1, n):
        abc.append((math.sqrt((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2), i, j))

abc.sort()
res = 0

for c,a,b in abc:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        res += c 

print(round(res, 2))
