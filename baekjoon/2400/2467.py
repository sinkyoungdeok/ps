N = int(input())
Y = list(map(int,input().split()))

start = 0
end = N-1
ans = 1000000000000
ans_start = 0
ans_end = 0


while start < end:
    if abs(Y[start] + Y[end]) < ans:
        ans = abs(Y[start] + Y[end])
        ans_start, ans_end = Y[start], Y[end]
    
    if Y[start] + Y[end] < 0:
        start += 1
    else:
        end -= 1

print(ans_start, ans_end)