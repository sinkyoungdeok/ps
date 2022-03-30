N = int(input())

res = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    res.append((age, i, name))

res.sort(key = lambda x : (x[0], x[1]))

for age, i, name in res:
    print(age, name)