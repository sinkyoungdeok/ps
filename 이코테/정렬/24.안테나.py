N = int(input())
nums = list(map(int, input().split()))

print(sorted(nums)[(N-1)//2])