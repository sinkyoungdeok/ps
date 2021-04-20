"""
문제 링크: https://www.acmicpc.net/problem/1946
문제 접근: 방법: 구현
"""

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    
    num_list = list(map(int, input().split()))
    
    P = []
    for i in range(len(num_list)):
        P.append( (i, num_list[i] ) )
    cnt = 1
    while 1 <= len(P):
        index, pri = P[0]
        del P[0]

        possible = True
        for i, p in P:
            if pri < p:
                possible = False
        if possible == False :
            P.append( (index,pri ))
        elif M == index:
            print(cnt)
        else:
            cnt +=1
        
