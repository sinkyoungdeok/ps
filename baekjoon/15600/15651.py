N, M = map(int, input().split())
temp = []


def dfs():
    if M == len(temp):
        print(' '.join(map(str, temp)))
        return

    for j in range(1, N + 1):
        temp.append(j)
        dfs()
        temp.pop()


dfs()
