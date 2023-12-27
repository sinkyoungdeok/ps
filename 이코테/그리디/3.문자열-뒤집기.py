S = list(map(int,list(input())))
    
res = [0,0]
res[S[0]] = 1

for i in range(len(S) - 1):
    if S[i] == S[i+1]:
        continue

    res[ S[i+1]^1 ] += 1

print(min(res))