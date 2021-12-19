N = int(input())

max_five = N // 5

res = 100000000

for i in range(0, max_five + 1):
    if (N- (i * 5) ) % 3 ==0:
        res = min(res, i + (N-(i * 5)) //3 )

if res == 100000000:
    res = -1
print(res)
