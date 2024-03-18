N, M = map(int, input().split())
temp = []


def dfs(i):
    if M == len(temp):
        print(' '.join(map(str, temp)))
        return

    for j in range(i, N + 1):
        temp.append(j)
        dfs(j)
        temp.pop()


dfs(1)
