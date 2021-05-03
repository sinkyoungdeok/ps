"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17679
문제 접근 방법: 구현
"""

def find_four(m, n, board):
    bomb_list = []

    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == '0':
                continue
            if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                bomb_list.append([i,j])
                bomb_list.append([i+1,j])
                bomb_list.append([i,j+1])
                bomb_list.append([i+1,j+1])

    return bomb_list

def bomb(bomb_list, board):
    res = 0
    for i,j in bomb_list:
        if board[i][j] != '0':
            res +=1
            board[i][j] = '0'
    return res

def falling(m,n,board):
    for _ in range(m):
        for j in range(m-1):
            for k in range(n):
                if board[j+1][k] == '0':
                    board[j+1][k] = board[j][k]
                    board[j][k] = '0'




def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    answer = 0
    while True:
        bomb_list = find_four(m,n,board)
        if len(bomb_list) == 0:
            break
        answer += bomb(bomb_list,board)
        falling(m,n,board)


    return answer

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m,n,board))