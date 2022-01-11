


"""
입력 (()[[]])
계산 2 * ( 2 + (3 * 3 ) )

depth = 0
( ==> [ (0, 2) ] , depth = 1
(( ==> [ (0,2), (1, 2) ] , depth = 2 
(() ==> [ (0,2), (1,2) ] , depth = 1
(()[ ==> [ (0,2), (1,2), (1,3) ], depth = 2
(()[[ ==> [ (0,2), (1,2), (1,3), (2,3) ], depth = 3
(()[[] ==> [ (0,2), (1,2), (1,3), (2,3) ], depth = 2
(()[[]] ==> [ (0,2), (1,2), (1, 9) ] ==> [ (0,2), (1, 11) ], depth = 1
(()[[]]) ==> [ (0, 22) ], depth = 0


"""

"""
입력 (()[[]])([])

depth = 0
( ==> [ (0,2) ], depth = 1
(( ==> [ (0,2), (1,2) ], depth = 2
(() ==> [ (0,2), (1,2) ], depth = 1
(()[ ==> [ (0,2), (1,2), (1,3) ], depth = 2
(()[[ ==> [ (0,2), (1,2), (1,3), (2,3) ], depth = 3
(()[[] ==> [ (0,2), (1,2), (1,3), (2,3) ], depth = 2 // 2까지 계산
(()[[]] ==> [ (0,2), (1,2), (1,9) ] ==> [ (0,2), (1, 11) ], depth = 1 // 1까지 계산
(()[[]]) ==> [ (0,22) ], depth = 0
(()[[]])( ==> 

"""

"""
결론.. depth가 2에서 1로 갈때 스택에 있는 1 depth들의 데이터를 계산한다. 즉 , depth가 내려갈때만 그  해당하는 depth까지 계산하면 됨 .
"""

S = input()

def calc(st, depth):
    while True:
        if len(st) < 2:
            break
        depth1, value1 = st.pop()
        depth2, value2 = st.pop()
        if depth1 >= depth and depth2 >= depth:
            if depth1 == depth2:
                value1 += value2
            else:
                value1 *= value2
            st.append((min(depth1, depth2), value1))
        else:
            st.append((depth2, value2))
            st.append((depth1, value1))
            break

def proof(S):
    st = []

    for i in S:
        if i == "(" or i == "[":
            st.append(i)
        elif i == ")":
            if len(st) == 0 or st[-1] != "(":
                return False
            st.pop()
        else:
            if len(st) == 0 or st[-1] != "[":
                return False
            st.pop()
    if len(st) > 0:
        return False

    return True


def solve():
    depth = 0
    st = []

    if not proof(S):
        return 0

    for i in S:
        if i == ")" or i == "]":
            depth -= 1
            calc(st, depth)
        elif i == "(":
            st.append((depth, 2))
            depth += 1
        elif i == "[":
            st.append((depth, 3))
            depth += 1

    return st[0][1]

print(solve())