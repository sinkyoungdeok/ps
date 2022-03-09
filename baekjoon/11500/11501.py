T = int(input())

def solve():
  ans = 0
  max_value = 0
  for i in range(len(joosicks)-1, -1, -1):
    if joosicks[i] > max_value:
      max_value = joosicks[i]
    else:
      ans += max_value - joosicks[i]
  return ans

for _ in range(T):
  N = int(input())
  joosicks = list(map(int, input().split()))
  print(solve())
