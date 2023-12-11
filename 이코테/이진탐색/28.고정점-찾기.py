N = int(input())
num_list = list(map(int, input().split()))

l, r = 0, N-1

check = True

while l <= r:
    m = (l+r) // 2

    if num_list[m] < m:
        l = m + 1
    elif num_list[m] > m:
        r = m - 1
    else:
        print(m)
        check = False
        break

if check:
    print(-1)