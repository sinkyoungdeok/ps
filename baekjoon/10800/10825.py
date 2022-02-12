N = int(input())

list = []

for _ in range(N):
    name, K, Y, S = input().split()
    K, Y, S = map(int, (K, Y, S))

    list.append((name, K, Y, S))

for name, K, Y, S in sorted(list, key=lambda x : (-x[1], x[2], -x[3], x[0])):
    print(name)
