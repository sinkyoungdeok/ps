"""
답은 맞았는데, 시간 초과 뜸.. python으론 안될듯 
"""

import math
from functools import cmp_to_key
import sys

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
    if cnt[num] == 1:
        return True
def erase(num, cnt):
    cnt[num] -= 1
    if cnt[num] == 0:
        return True
        
dic = {}
dic_i = 1
N = int(sys.stdin.readline())
A = []
for i in sys.stdin.readline().split():
    i = int(i)
    if not dic.get(i):
        dic[i] = dic_i
        dic_i +=1
    A.append(dic[i])
M = int(sys.stdin.readline())
cnt = [0] * 1000011
ans = [0] * 1000011

sqrtN = math.sqrt(N)

query = [] 
for i in range(M):
    u,v = map(int,sys.stdin.readline().split())    
    query.append((u-1,v-1,i))


query.sort(key = cmp_to_key(compare))


prev_l = 0
prev_r = 0
res = 0
if add(A[0], cnt):
    res += 1


for i in range(M):
    next_l = query[i][0]
    next_r = query[i][1]

    for j in range(prev_l, next_l):
        if erase(A[j], cnt):
            res -= 1
    for j in range(prev_l - 1, next_l - 1, -1):
        if add(A[j], cnt):
            res +=1
    for j in range(prev_r + 1, next_r + 1):
        if add(A[j], cnt):
            res +=1
    for j in range(prev_r, next_r, -1):
        if erase(A[j], cnt):
            res -=1
    
    prev_l, prev_r = next_l, next_r
    ans[query[i][2]] = res 

for i in range(M):
    print(ans[i])
