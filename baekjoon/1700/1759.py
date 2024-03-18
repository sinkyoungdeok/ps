M, N = map(int, input().split())
nums = sorted(list(input().split()))
temp = []


def dfs(i):
  if M == len(temp):
    if temp.count('a') + temp.count('e') + temp.count('i') + temp.count('o') + temp.count('u') < 1:
        return
    if M - (temp.count('a') + temp.count('e') + temp.count('i') + temp.count('o') + temp.count('u')) < 2:
        return
    print(''.join(map(str, temp)))
    return

  for j in range(i, N + 1):
    temp.append(nums[j-1])
    dfs(j + 1)
    temp.pop()


dfs(1)
