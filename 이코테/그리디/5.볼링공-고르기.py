N, M = map(int, input().split())
K = sorted(list(map(int, input().split())))

res = 0
for i in range(N):
    for j in range(i+1, N):
        if K[i] == K[j]:
            continue
            
        res += N - j
        break

print(res)