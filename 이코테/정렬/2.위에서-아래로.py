N = int(input())
nums = [ int(input()) for _ in range(N)]

for i in sorted(nums, reverse=True):
    print(i, end=' ')