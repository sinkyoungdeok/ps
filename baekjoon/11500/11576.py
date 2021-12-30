A, B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))[::-1]

sum = 0

for i in range(len(nums)):
    sum += nums[i] * (A**i)

res = []
while sum != 0:
    res.append(sum % B)
    sum //= B 

print(" ".join(map(str, res[::-1])))