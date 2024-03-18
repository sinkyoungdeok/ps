N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []


def dfs(i):
    if M == len(temp):
        print(' '.join(map(str, temp)))
        return

    for j in range(i, N + 1):
        temp.append(nums[j-1])
        dfs(j + 1)
        temp.pop()


dfs(1)
