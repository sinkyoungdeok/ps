def dfs(i):
  if 6 == len(temp):
    print(' '.join(map(str, temp)))
    return

  for j in range(i, N + 1):
    temp.append(nums[j - 1])
    dfs(j + 1)
    temp.pop()


while True:
  nums = list(map(int, input().split()))

  if nums[0] == 0:
    break

  nums = nums[1:]
  N = len(nums)

  temp = []

  dfs(1)
  print()
