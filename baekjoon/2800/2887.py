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

N = int(input())
parent = [i for i  in range(N+1)]

X = []
Y = []
Z = []

for i in range(1, N+1):
    x,y,z = map(int, input().split())
    X.append((x,i))
    Y.append((y,i))
    Z.append((z,i))

X.sort()
Y.sort()
Z.sort()

XYZ = []

for i in range(N-1):
    XYZ.append( (abs(X[i+1][0] - X[i][0]), X[i][1], X[i+1][1] ) )
    XYZ.append( (abs(Y[i+1][0] - Y[i][0]), Y[i][1], Y[i+1][1] ) )
    XYZ.append( (abs(Z[i+1][0] - Z[i][0]), Z[i][1], Z[i+1][1] ) )

XYZ.sort()
res = 0

for c,a,b in XYZ:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += c

print(res)