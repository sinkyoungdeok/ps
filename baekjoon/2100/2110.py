N, C = map(int, input().split())
x = [ int(input()) for _ in range(N)]
x.sort()

l, r = 0, 1000000000

while l <= r:
    m = (l+r) // 2

    temp = x[0]
    cnt = 1
    for i in range(1, N):
        if (x[i] - temp) >= m:
            temp = x[i]
            cnt += 1

    if cnt >= C:
        l = m + 1
    else:
        r = m - 1

print(r)
