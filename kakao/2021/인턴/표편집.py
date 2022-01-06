def solution(n, k, cmd):
    answer = ''
    linked_list = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    res = ['0'] * n
    curr = k + 1
    st = []

    for c in cmd:
        if len(c) == 0:  # C or Z
            if c == 'C':
                prev, next = linked_list[curr]
                st.append([prev, curr, next])
                res[curr - 1] = 'X'
                if next == n + 1:
                    curr = linked_list[curr][0]
                else:
                    curr = linked_list[curr][1]

                if prev == 0:
                    linked_list[next][0] = prev
                elif next == n + 1:
                    linked_list[prev][1] = next
                else:
                    linked_list[prev][1] = next
                    linked_list[next][0] = prev
            else:
                prev, cur, next = st.pop()
                res[cur - 1] = '0'

                if prev == 0:
                    linked_list[next][0] = cur
                elif next == n + 1:
                    linked_list[prev][1] = cur
                else:
                    linked_list[prev][1] = cur
                    linked_list[next][0] = cur

        else:  # D or U
            ud, num = c.split()
            num = int(num)

            if ud == 'D':
                for _ in range(num):
                    curr = linked_list[curr][1]
            else:
                for _ in range(num):
                    curr = linked_list[curr][0]

    for i in res:
        answer += i

    return answer

solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])