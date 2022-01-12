from collections import deque

def spring_and_summer():
    for i in range(N):
        for j in range(N):
            q_len = len(Q[i][j])
            for k in range(q_len):
                if Q[i][j][k] <= Y[i][j]:
                    Y[i][j] -= Q[i][j][k]
                    Q[i][j][k] += 1
                else:
                    for _ in range(k, q_len):
                        Y[i][j] += Q[i][j].pop() // 2
                    break


def fall_and_winter():
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(N):
        for j in range(N):
            for k in Q[i][j]:
                if k % 5 != 0:
                    continue
                for d in range(8):
                    r = i + dr[d]
                    c = j + dc[d]
                    if 0 <= r < N and 0 <= c < N:
                        Q[r][c].appendleft(1)
            Y[i][j] += A[i][j]



N, M, K = map(int,input().split())
A = []
Q = [[deque() for i in range(N)] for i in range(N)]
Y = [[5] * N for i in range(N)]

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(M):
    x,y,z = map(int, input().split())
    Q[x-1][y-1].append(z)

for i in range(K):
    spring_and_summer()
    fall_and_winter()

res = 0
for i in range(N):
    for j in range(N):
        res += len(Q[i][j])

print(res)