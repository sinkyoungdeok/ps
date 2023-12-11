from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
num_list = list(map(int, input().split()))

ans = bisect_right(num_list,x) - bisect_left(num_list, x)

if ans == 0:
    print(-1)
else:
    print(ans)