N, M = map(int, input().split())
num_list = [[False] * N for _ in range(N)]

for i in range(M):
    a,b = map(int, input().split())
    num_list[a-1][b-1] = True
    num_list[b-1][a-1] = True


res = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if not num_list[i][j] and not num_list[i][k] and not num_list[j][k]:
                res += 1

print(res)