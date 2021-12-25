st = []

while True:
    input_ = list(map(int, input().split()))
    if input_[0] == 0:
        break
    n = input_[0]
    h = input_[1:]
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


