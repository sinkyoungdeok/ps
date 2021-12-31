N = int(input())
start = 0 
end = 1
ans = 0 
sum = 1 

while start < N//2 + 1:
    if sum < N: 
        end += 1
        sum += end
    elif sum == N: 
        ans += 1
        end += 1
        sum -= start
        sum += end
        start += 1
    else: 
        sum -= start
        start += 1
        
print(ans + 1) 