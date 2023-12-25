N = int(input())

res, cnt = 0, 0
for p in sorted(list(map(int, input().split()))):
    cnt += 1
    if cnt >= p:
        res += 1
        cnt = 0

print(res)