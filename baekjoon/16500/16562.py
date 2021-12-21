import sys

sys.setrecursionlimit(10 ** 9)

N,M,k = map(int, input().split())
A = list(map(int, input().split()))

adj = [ [] for _ in range(N) ]
check = [False] * N 
ans = []

for i in range(M):
    v,w = map(int, input().split())
    adj[v-1].append(w-1)
    adj[w-1].append(v-1)

def dfs(idx, friends):
    check[idx] = True
    for i in adj[idx]:
        if check[i]:
            continue
        friends.append(i)
        dfs(i, friends)
    return friends 

for i in range(N):
    if check[i]:
        continue
    friends = dfs(i, [i])
    temp = 100000000000
    for j in friends:
        temp = min(temp, A[j])
    ans.append(temp)

if sum(ans) <= k:
    print(sum(ans))
else:
    print("Oh no")
    
