N = int(input())

x, y = [], []

for _ in range(N):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

x = x + [x[0]]
y = y + [y[0]]

ans = 0
for i in range(N):
    ans += (x[i]*y[i+1]) - (x[i+1]*y[i])
    
print(round(abs(ans)/2,1))