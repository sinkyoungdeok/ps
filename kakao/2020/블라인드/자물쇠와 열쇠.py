import copy

def play(lock, key, i, j, M, N):
    for ii in range(M):
        for jj in range(M):
            lock[ii + i][jj +j ] += key[ii][jj]
    
    for i in range(N):
        for j in range(N):
            if lock[M+i][M+j] != 1:
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)
    
    LOCK = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    for i in range(N):
        for j in range(N):
            LOCK[M+i][M+j] = lock[i][j]
    
    for _ in range(4):
        key = list(zip(*key[::-1]))
        
        for i in range(1, M+N):
            for j in range(1, M+N):
                if(play(copy.deepcopy(LOCK), key, i, j, M, N)):
                    return True
    
    
    return False