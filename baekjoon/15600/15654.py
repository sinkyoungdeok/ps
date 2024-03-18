N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []


def dfs():
    if M == len(temp):
        print(' '.join(map(str, temp)))
        return

    for j in range(1, N + 1):
        if nums[j-1] in temp:
            continue
        temp.append(nums[j-1])
        dfs()
        temp.pop()


dfs()
