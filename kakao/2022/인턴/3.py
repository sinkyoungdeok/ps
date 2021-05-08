"""
U X: 현재행에서 X칸 위에있는 행 선택
D X: 현재행에서 X칸 아래있는 행 선택
C: 현재 행 삭제후, 바로 아래 행 선택. 삭제된행이 마지막이면 윗행을 선택
Z: 최근에 삭제된 행을 복구. 선택된 행은 그대로
"""
def solution(n, k, cmd):
    answer = ['O'] * n


    delete_list = []

    for c in cmd:
        if c[0] == 'D':
            X = int(c.split()[1])
            for i in range(X):
                while True:
                    k +=1
                    if answer[k] == 'O':
                        break
        elif c[0] == 'U':
            X = int(c.split()[1])
            for i in range(X):
                while True:
                    k -=1
                    if answer[k] == 'O':
                        break
        elif c[0] == 'C':
            answer[k] = 'X'
            delete_list.append(k)
            last_check = True
            for i in range(k+1, n):
                if answer[i] == 'O':
                    last_check = False
                    k = i
                    break
            if last_check:
                while True:
                    k -=1
                    if answer[k] == 'O':
                        break
        else:
            delete_index = delete_list.pop()
            answer[delete_index] = 'O'

    return ''.join(answer)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))