from collections import deque

dq = deque()
dq.append((0, 0))

N = int(input())
K = int(input())

board = [[False] * N for _ in range(N)]

for i in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = True

L = int(input())
rotate = [''] * 10001

for i in range(L):
    X, C = input().split()
    rotate[int(X)] = C

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
D_index = 0  # 0 -> 1 -> 2 -> 0
cnt = 0


def is_game_end(next_i, next_j):
    if not (0 <= next_i < N and 0 <= next_j < N):
        return True

    for i, j in dq:
        if i == next_i and j == next_j:
            return True

    return False


while True:
    curr_i, curr_j = dq[0]
    next_i, next_j = curr_i + D[D_index][0], curr_j + D[D_index][1]  # 한칸 이동
    cnt += 1

    if is_game_end(next_i, next_j):
        break

    if not board[next_i][next_j]:
        dq.pop()

    dq.appendleft((next_i, next_j))
    board[next_i][next_j] = False

    if rotate[cnt] == 'D':
        D_index += 1
        D_index %= 4
    elif rotate[cnt] == 'L':
        D_index = 3 if D_index == 0 else D_index - 1

print(cnt)
