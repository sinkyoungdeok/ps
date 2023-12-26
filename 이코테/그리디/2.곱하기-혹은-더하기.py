S = list(map(int,sorted(list(input()))))

res = prev = S[0]
for i in S[1:]:
    if prev <= 1:
        res += i
    else:
        res *= i
    prev = i

print(res)