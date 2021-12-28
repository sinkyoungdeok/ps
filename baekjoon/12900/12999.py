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

def add(num, cnt, cnt2, max_cnt):
    if cnt[num]:
        cnt2[cnt[num]] -=1
    cnt[num] += 1
    cnt2[cnt[num]] +=1
    if cnt2[max_cnt + 1] > 0 :
        max_cnt += 1
    return max_cnt
    

    return max(max_cnt, cnt[num])
def erase(num, cnt, cnt2, max_cnt):
    cnt2[cnt[num]] -= 1
    cnt2[cnt[num] - 1] += 1
    cnt[num] -= 1
    if cnt2[max_cnt] <= 0 :
        max_cnt -= 1
    return max_cnt
        

N, M = map(int, input().split())
A = [int(i) + 100001 for i in input().split()]
cnt = [0] * 200022
cnt2 = [0] * 200022
ans = [0] * 200022

sqrtN = math.sqrt(N)

query = [] 
for i in range(M):
    u,v = map(int,input().split())    
    query.append((u-1,v-1,i))


query.sort(key = cmp_to_key(compare))


prev_l = 0
prev_r = 0
max_cnt = add(A[0], cnt, cnt2, 0)

for i in range(M):
    next_l = query[i][0]
    next_r = query[i][1]

    for j in range(prev_l, next_l):
        max_cnt = erase(A[j], cnt, cnt2, max_cnt)
    for j in range(prev_l - 1, next_l - 1, -1):
        max_cnt = add(A[j], cnt, cnt2, max_cnt) 
    for j in range(prev_r + 1, next_r + 1):
        max_cnt = add(A[j], cnt, cnt2, max_cnt) 
    for j in range(prev_r, next_r, -1):
        max_cnt = erase(A[j], cnt, cnt2, max_cnt)
    
    prev_l, prev_r = next_l, next_r
    ans[query[i][2]] = max_cnt 

for i in range(M):
    print(ans[i])
