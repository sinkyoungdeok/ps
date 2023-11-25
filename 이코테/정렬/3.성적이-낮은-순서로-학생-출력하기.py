N = int(input())

res = []
for _ in range(N):
    name, score = input().split()
    res.append((name, int(score)))

for _, score in sorted(res, key=lambda x: x[1]):
    print(name, end=' ')