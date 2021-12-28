import math
from functools import cmp_to_key

def compare(a,b):
    if a[0]//sqrtN != b[0]//sqrtN:
        if a[0]//sqrtN > b[0]//sqrtN:
            return 1
        elif a[0]//sqrtN == b[0]//sqrtN:
            return 0
        else:
            return -1 
    
    if a[1] > b[1]:
        return 1
    elif a[1] == b[1]:
        return 0
    else:
        return -1 

def add(num, cnt):
    cnt[num] += 1

def erase(num, cnt):
    cnt[num] -= 1
        

N, C = map(int, input().split())
A = list(map(int,input().split()))
M = int(input())
cnt = [0] * 100001
ans = [0] * 100001

sqrtN = math.sqrt(N)

query = [] 
for i in range(M):
    u,v = map(int,input().split())    
    query.append((u-1,v-1,i))


query.sort(key = cmp_to_key(compare))


prev_l = 0
prev_r = 0
add(A[0], cnt)

for i in range(M):
    next_l = query[i][0]
    next_r = query[i][1]

    for j in range(prev_l, next_l):
        erase(A[j], cnt)
    for j in range(prev_l - 1, next_l - 1, -1):
        add(A[j], cnt)
    for j in range(prev_r + 1, next_r + 1):
        add(A[j], cnt)
    for j in range(prev_r, next_r, -1):
        erase(A[j], cnt)
    
    prev_l, prev_r = next_l, next_r

    check = 0
    for j in range(1,C+1):
        if cnt[j] > (next_r - next_l + 1)//2: 
            check = j
            break 
    
    if check == 0:
        ans[query[i][2]] = "no"
    else:
        ans[query[i][2]] = "yes " + str(check)

for i in range(M):
    print(ans[i])
