N = int(input())
nums = list(map(int, input().split()))

print(sorted(nums)[N//2-1])