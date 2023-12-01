N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))

st = []

sum = A[0]
index = 1

st.append( (sum, index, O) )

res_min = 10000000000000000
res_max = -10000000000000000 

while st:
    c_sum, c_i, c_o = st.pop()

    if c_i == N:
        res_min = min(res_min, c_sum)
        res_max = max(res_max, c_sum) 
        continue
    
    next_num = A[c_i]
    next_index = c_i + 1
    
    for i, oper in enumerate(c_o):
        if oper == 0 :
            continue 

        if i == 0: # + 
            st.append((c_sum + next_num, next_index, [c_o[0]-1, c_o[1], c_o[2], c_o[3] ] ))
        elif i == 1: # -
            st.append((c_sum - next_num, next_index, [c_o[0], c_o[1]-1, c_o[2], c_o[3] ] ))
        elif i == 2: # *
            st.append((c_sum * next_num, next_index, [c_o[0], c_o[1], c_o[2]-1, c_o[3] ] ))
        else: # /
            if c_sum < 0:
                st.append(( -((-c_sum) // next_num), next_index, [c_o[0], c_o[1], c_o[2], c_o[3]-1 ] ))
            else:
                st.append(( c_sum // next_num, next_index, [c_o[0], c_o[1], c_o[2], c_o[3]-1 ] ))

print(res_max)
print(res_min)