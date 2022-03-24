from collections import deque

N, M, V = map(int, input().split())

adj = [ [] for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

# stack 

for i in range(N):
    adj[i].sort(reverse = True)

st_visited = [False] * N

st = deque()
st.append(V-1)

while st:
    curr = st.pop()

    if st_visited[curr]:
            continue
    st_visited[curr] = True 
    print(curr+1, end= " ")

    for next in adj[curr]:
        st.append(next)

print()

# queue

for i in range(N):
    adj[i].sort()

q_visited = [False] * N

q = deque()
q.append(V-1)
q_visited[V-1] = True

while q:
    curr = q.popleft()
    
    print(curr+1, end= " ")

    for next in adj[curr]:
        if q_visited[next]:
            continue

        q_visited[next] = True 
        q.append(next)


