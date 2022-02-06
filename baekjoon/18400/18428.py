from itertools import combinations

N = int(input())
board = [input().split() for _ in range(N) ]

T = []
O = []
D = [ (0,1), (1,0), (0,-1), (-1,0) ]

for i in range(N):
    for j in range(N):
        if board[i][j] == "X":
            O.append((i,j))
        elif board[i][j] == "T":
            T.append((i,j))

check = True

def simul():
    for ti, tj in T:
        for d in range(4):
            if search(ti, tj, d):
                return False
    return True

def search(ci, cj, d):
    if board[ci][cj] == "S":
        return True
    if board[ci][cj] == "O":
        return False 
    ni, nj = ci + D[d][0], cj + D[d][1]
    if not (0<= ni < N and 0 <= nj < N):
        return False
    
    return search(ni,nj,d)
    
for o in combinations(O, 3):
    for oi,oj in o:
        board[oi][oj] = "O"
    if simul():
        check = False
        print("YES")
        break
    for oi,oj in o:
        board[oi][oj] = "X"
        
if check:
    print("NO")
