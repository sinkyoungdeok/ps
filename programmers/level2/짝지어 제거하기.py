def solution(s): 
    st = []
    for i in s:
        if len(st) == 0: 
            st.append(i)
        elif st[-1] == i: 
            st.pop()
        else: 
            st.append(i)
    if len(st) == 0:
        return 1
    return 0 