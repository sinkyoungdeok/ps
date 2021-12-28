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

def add(num, cnt,res):
    if cnt[num] == 2:
        res -=1
    cnt[num]+=1
    if cnt[num] == 2:
        res +=1
    return res 
        
        
def erase(num, cnt,res):
    if cnt[num] == 2:
        res -=1
    cnt[num]-=1
    if cnt[num] == 2:
        res +=1
    return res
        
dic = {}
dic_i = 1
N, M = map(int, input().split())
A = []
for i in input().split():
    i = int(i)
    if not dic.get(i):
        dic[i] = dic_i
        dic_i +=1
    A.append(dic[i])
cnt = [0] * 1000001
ans = [0] * 1000001

sqrtN = math.sqrt(N)

query = [] 
for i in range(M):
    u,v = map(int,input().split())    
    query.append((u-1,v-1,i))


query.sort(key = cmp_to_key(compare))


prev_l = 0
prev_r = 0
res = add(A[0], cnt, 0)

for i in range(M):
    next_l = query[i][0]
    next_r = query[i][1]

    for j in range(prev_l, next_l):
        res = erase(A[j], cnt, res)
    for j in range(prev_l - 1, next_l - 1, -1):
        res = add(A[j], cnt, res)
    for j in range(prev_r + 1, next_r + 1):
        res = add(A[j], cnt, res)
    for j in range(prev_r, next_r, -1):
        res = erase(A[j], cnt, res)
    
    prev_l, prev_r = next_l, next_r
    ans[query[i][2]] = res 

for i in range(M):
    print(ans[i])
