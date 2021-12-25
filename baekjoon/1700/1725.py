st = []


n = int(input())
h = [ int(input()) for _ in range(n)]
ans = []
for i in range(len(h)):
    start = i

    while st and st[-1][0] > h[i]:
        height, idx = st.pop()
        ans.append(height * (i - idx))
        start = idx
    st.append((h[i], start))

while st:
    height, idx = st.pop()
    ans.append(height * (n - idx))

print(max(ans))


